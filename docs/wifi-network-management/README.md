# Wi-Fi management / Zarządzanie Wi-Fi

**Experimental / Eksperymentalne** — CA2RXU upstream, GPL-3.0-or-later. Target ESP32 / Heltec V3.1.

## PL
Indywidualny DHCP lub statyczny IPv4 dla każdej sieci: IP, brama, maska, DNS1 i opcjonalny DNS2. Brak nowego pola w starszym JSON oznacza DHCP. Kolejność sieci pozostaje bez zmian. Brak IP oznacza nieudane połączenie. Nie instalować na bramce produkcyjnej przed testami.

Testy: stary JSON, DHCP, statyczny IPv4 bez DHCP, przełączenie przy braku DHCP, static -> DHCP, błędny IP, usunięcie środkowego profilu, restart, backup/restore, Auto AP, regresja W5500. Zachować kopię i dostęp USB. Walidacja podsieci, priorytety i kontrola APRS-IS pozostają do wykonania.

## EN
Per-network DHCP or static IPv4: IP, gateway, subnet, primary and optional secondary DNS. Older JSON defaults to DHCP. Existing network order retained. Missing IP means failed connection. Do not flash a production gateway before testing.

Tests: legacy JSON, DHCP, static-only AP, DHCP failure and next AP, static-to-DHCP, invalid IP, deleting middle profile, reboot, backup/restore, Auto AP, W5500 regression. Keep a backup and USB recovery. Subnet validation, priorities and APRS-IS health checks remain future work.
