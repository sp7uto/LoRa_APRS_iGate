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
    for key, val in {"callsign":"SP0ABC-10","passcode":"12345","lat":"51.5","lon":"18.7"}.items():
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
    assert c["lora"]["txActive"] is False
    assert c["digi"]["backupDigiMode"] is False
    assert c["wifi"]["aprsFailover"] is True
    assert c["wifi"]["AP"][1]["ip"] == "192.168.2.50"
    assert c["webadmin"]["active"] is True
    assert len({c["webadmin"]["password"], c["ota"]["password"], c["wifi"]["autoAP"]["password"]}) == 3
    assert not errors, errors
    assert not external, external
    browser.close()
print("Browser export passed; no external requests")
