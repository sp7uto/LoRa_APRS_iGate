"""Test local browser export; no connection to a live gateway."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parents[1]
with sync_playwright() as p, TemporaryDirectory() as tmp:
    browser = p.chromium.launch()
    page = browser.new_page(accept_downloads=True)
    errors = []
    external = []
    page.on("pageerror", lambda err: errors.append(str(err)))
    def block(route):
        external.append(route.request.url)
        route.abort()
    page.route("http**/*", block)
    page.goto((root / "docs/config-generator/index.html").as_uri())
    for key, val in {"callsign":"SP0ABC-10","passcode":"12345","lat":"51°35.42′ N","lon":"01844.22E"}.items():
        page.locator("#"+key).fill(val)
    first = page.locator(".network").first
    first.locator('[data-field="ssid"]').fill("Example-AP")
    first.locator('[data-field="password"]').fill("example-pass")
    page.locator("#preset").select_option("local")
    page.locator("#confirmRadio").check()
    page.locator("button[type=submit]").click()
    assert page.locator("#download").is_enabled(), page.locator("#result").inner_text()
    page.locator("#add").click()
    assert not page.locator("#download").is_enabled()
    second = page.locator(".network").nth(1)
    second.locator('[data-field="ssid"]').fill("Backup-AP")
    second.locator('[data-field="password"]').fill("example-pass")
    second.locator('[data-field="dhcp"]').select_option("0")
    second.locator('[data-field="ip"]').fill("192.168.2.50")
    second.locator('[data-field="gateway"]').fill("192.168.2.1")
    page.locator("#failover").check()
    page.locator("button[type=submit]").click()
    assert page.locator("#download").is_enabled(), page.locator("#result").inner_text()
    with page.expect_download() as d:
        page.locator("#download").click()
    target = Path(tmp) / "config.json"
    d.value.save_as(target)
    c = json.loads(target.read_text())
    assert abs(c["beacon"]["latitude"] - (51+35.42/60)) < 1e-10
    assert abs(c["beacon"]["longitude"] - 18.737) < 1e-10
    assert c["lora"]["txActive"] is False
    assert c["digi"]["backupDigiMode"] is False
    assert c["wifi"]["aprsFailover"] is True
    assert c["wifi"]["AP"][1]["ip"] == "192.168.2.50"
    assert c["webadmin"]["active"] is True
    assert len({c["webadmin"]["password"], c["ota"]["password"], c["wifi"]["autoAP"]["password"]}) == 3
    # Existing backup: unchanged export, then explicit migration and profile change.
    legacy = json.loads(target.read_text())
    legacy["unknownFutureSection"] = {"flag": True}
    legacy["mqtt"]["password"] = "keep-this-secret"
    legacy["wifi"]["AP"][0].pop("dhcp")
    legacy["wifi"].pop("aprsFailover")
    src = Path(tmp) / "legacy.json"
    src.write_text(json.dumps(legacy))
    page.locator("#importFile").set_input_files(str(src))
    page.locator("#editPanel").wait_for(state="visible")
    page.locator("#reviewEdit").click()
    assert page.locator("#downloadEdit").is_enabled(), page.locator("#editResult").inner_text()
    with page.expect_download() as d:
        page.locator("#downloadEdit").click()
    result = Path(tmp) / "unchanged.json"
    d.value.save_as(result)
    assert json.loads(result.read_text()) == legacy
    page.locator("#upgradeWifi").click()
    page.locator('[data-path="wifi.AP.0.dhcp"]').select_option("true")
    page.locator('[data-path="beacon.comment"]').fill("Modified beacon")
    page.locator('[data-path="beacon.latitude"]').fill("52°15′30″ N")
    page.locator('[data-path="beacon.longitude"]').fill("18,75")
    page.locator("#editProfile").select_option("wide1")
    page.locator("#applyProfile").click()
    page.locator("#reviewEdit").click()
    assert not page.locator("#downloadEdit").is_enabled()
    page.locator("#editConfirmRF").check()
    page.locator("#reviewEdit").click()
    assert page.locator("#downloadEdit").is_enabled(), page.locator("#editResult").inner_text()
    with page.expect_download() as d:
        page.locator("#downloadEdit").click()
    result = Path(tmp) / "modified.json"
    d.value.save_as(result)
    mod = json.loads(result.read_text())
    assert mod["unknownFutureSection"] == legacy["unknownFutureSection"]
    assert mod["mqtt"]["password"] == legacy["mqtt"]["password"]
    assert mod["wifi"]["AP"][0]["password"] == legacy["wifi"]["AP"][0]["password"]
    assert mod["beacon"]["comment"] == "Modified beacon"
    assert abs(mod["beacon"]["latitude"] - (52+15/60+30/3600)) < 1e-10
    assert mod["beacon"]["longitude"] == 18.75
    assert mod["digi"]["mode"] == 1 and mod["lora"]["txActive"] is True
    assert "keep-this-secret" not in page.locator("#editDiff").inner_text()
    assert not errors, errors
    assert not external, external
    browser.close()
print("Browser export passed; no external requests")
