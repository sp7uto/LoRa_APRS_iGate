"""Render actual firmware Wi-Fi configuration controls with fictional sample data."""
from pathlib import Path
import argparse
from playwright.sync_api import sync_playwright

parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
assets = root / "data_embed"
html = (assets / "index.html").read_text(encoding="utf-8")
js = (assets / "script.js").read_text(encoding="utf-8")
start = js.index("function reindexWiFiNetworks()")
end = js.index('document.querySelector(".new button").addEventListener', start)
# Use the actual DOM builder; isolate it from network calls and hardware APIs.
builder = js[start:end]
css = (assets / "bootstrap.css").read_text(encoding="utf-8")
style = (assets / "style.css").read_text(encoding="utf-8")
args.output.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1200, "height": 1400},
                            device_scale_factor=1.5, color_scheme="dark")
    page.route("**/*", lambda route: route.abort())
    # Prevent scripts and external resources from running; keep firmware inline styles.
    import re
    isolated = re.sub(r"<script\b[^>]*>.*?</script\s*>", "", html,
                      flags=re.IGNORECASE | re.DOTALL)
    page.set_content(isolated, wait_until="domcontentloaded")
    page.add_style_tag(content=css)
    page.add_style_tag(content=style)
    page.evaluate("""() => {
        document.documentElement.setAttribute("data-bs-theme", "dark");
        document.documentElement.removeAttribute("data-variant");
        const access = [...document.querySelectorAll("h5")].find(x => x.textContent.trim() === "WiFi Access").closest(".row.my-5");
        const auto = [...document.querySelectorAll("h5")].find(x => x.textContent.trim() === "WiFi Auto AP").closest(".row.my-5");
        if (!access || !auto) throw Error("Missing Wi-Fi configuration section");
        const panel = document.createElement("main");
        panel.id = "doc-preview";
        panel.className = "container";
        panel.style.cssText = "padding:24px 32px;width:1120px;max-width:1120px;margin:0 auto";
        access.classList.remove("my-5");
        auto.classList.remove("my-5");
        auto.style.marginTop = "30px";
        const title = document.createElement("div");
        title.style.cssText = "background:#b21d1d;color:white;font-weight:600;font-size:20px;padding:12px 16px;margin-bottom:24px;border-radius:6px";
        title.textContent = "LoRa APRS iGate — Connectivity";
        panel.append(title, access, auto);
        document.body.replaceChildren(panel);
        document.getElementById("startupDelay").value = "0";
        document.getElementById("wifi.autoAP.enabled").checked = true;
        document.getElementById("wifi.autoAP.password").value = "example-only";
        document.getElementById("wifi.autoAP.timeout").value = "10";
        document.getElementById("wifi-autoap-config").style.display = "block";
        document.getElementById("wifi.aprsFailover").checked = true;
    }""")
    page.add_script_tag(content=builder)
    dhcp = {"ssid":"Home-AP", "password":"example-only", "dhcp":True}
    static = {"ssid":"Remote-AP", "password":"example-only", "dhcp":False,
              "ip":"192.168.2.50", "gateway":"192.168.2.1",
              "subnet":"255.255.255.0", "dns1":"9.9.9.9", "dns2":"1.1.1.1"}
    for filename, profiles in [
        ("ap-dhcp.png", [dhcp]),
        ("ap-static-ipv4.png", [static]),
        ("ap-priority-failover.png", [dhcp, static]),
    ]:
        page.evaluate("""profiles => {
            document.querySelector(".list-networks").replaceChildren();
            profiles.forEach(profile => appendWiFiNetwork(profile));
            document.getElementById("wifi.aprsFailover").checked = profiles.length > 1;
            document.getElementById("wifi-autoap-config").closest(".row.my-5")?.removeAttribute("hidden");
        }""", profiles)
        fields = page.locator(".network").count()
        assert fields == len(profiles), "Unexpected number of AP profiles"
        assert page.locator(".network [data-wifi-field='ip']:visible").count() == sum(not n["dhcp"] for n in profiles)
        # Two focused AP images; third includes Auto AP and the failover checkbox.
        auto = page.locator("#wifi-autoap-config").locator("xpath=ancestor::div[contains(@class,'align-items-top')][1]")
        auto.evaluate("(el, show) => { el.hidden = !show; if (!show) el.style.setProperty('display','none','important'); else el.style.removeProperty('display'); }", len(profiles)>1)
        page.locator("#doc-preview").screenshot(path=str(args.output / filename), animations="disabled")
    browser.close()
