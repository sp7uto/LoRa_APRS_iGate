"""Insert the approved cover once its versioned image exists."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
asset = root / "docs/wifi-network-management/wiki/images/sp7uto/igate-cover.jpg"
if not asset.is_file():
    print("Cover asset not uploaded; keeping existing illustrations")
    raise SystemExit(0)
caption = "*Mapa poglądowa — przykładowe stacje, pozycje, odległości i zasięg, nie dane z pomiarów. / Illustrative map — example stations, positions, distances and coverage, not measured data.*"
for rel, image in [
    ("README.md", "docs/wifi-network-management/wiki/images/sp7uto/igate-cover.jpg"),
    ("docs/wifi-network-management/README.md", "wiki/images/sp7uto/igate-cover.jpg"),
    ("docs/wifi-network-management/wiki/Home.md", "images/sp7uto/igate-cover.jpg"),
]:
    path = root / rel
    text = path.read_text(encoding="utf-8")
    if "igate-cover.jpg" in text:
        continue
    title, sep, rest = text.partition("\n")
    assert sep and title.startswith("# "), rel
    banner = "![SP7UTO-10 — LoRa APRS iGate in Sieradz](" + image + ")"
    path.write_text(title + "\n\n" + banner + "\n\n" + caption + "\n" + rest, encoding="utf-8")
    print("Cover inserted:", rel)
