# 🛠️ Diagnostyka / Troubleshooting

| Objaw / Symptom | Sprawdź / Check |
|---|---|
| Wi-Fi bez IP / Wi-Fi no IP | DHCP availability; try a correctly configured static profile |
| Static IP rejected | Address, contiguous mask, gateway on same subnet, DNS |
| IP but APRS-IS offline | Gateway, DNS, Internet route, server/port, passcode |
| Wrong network selected | Profile order and duplicate SSIDs |
| No configured network connects | Auto AP and USB recovery |
| CI fails | Build logs and target environment |

PL: Zmieniaj pojedyncze ustawienia i zachowuj kopie. Nie włączaj TX w celu diagnostyki problemu sieciowego.
EN: Change one setting at a time and retain backups. Do not enable TX to diagnose a network problem.
