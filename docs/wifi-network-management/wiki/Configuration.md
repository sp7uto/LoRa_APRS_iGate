# Konfiguracja / Configuration


![Original CA2RXU Web UI menu](images/ca2rxu/web-menu.png)

*Menu oryginalnego firmware; nowe pola IPv4 i failover opisano niżej / Upstream menu; new fork settings are described below — [CA2RXU upstream](https://github.com/richonguzman/LoRa_APRS_iGate).*

PL: Connectivity → WiFi Access → Add network. Wpisz SSID i hasło. Wybierz DHCP lub Static IPv4. W trybie statycznym podaj wolny adres urządzenia, maskę, bramę i DNS1; DNS2 jest opcjonalny. Brama musi leżeć w tej samej podsieci. Move up / Move down ustala kolejność prób. Zachowaj Auto AP jako drogę odzyskania.

EN: Connectivity → WiFi Access → Add network. Enter SSID and passphrase, then DHCP or Static IPv4. For static addressing supply an unused IP, subnet mask, gateway and primary DNS; secondary DNS is optional. Gateway must be on the same subnet. Use Move up / Move down to set connection order. Keep Auto AP enabled for recovery.

Example only / Przykład (nie kopiować bez sprawdzenia): 192.168.2.50, 255.255.255.0, gateway 192.168.2.1, DNS 9.9.9.9.

## Experimental APRS-IS WiFi failover

PL: Domyślnie OFF. Włączenie jest opcjonalne po testach podstawowych. Wymaga minimum dwóch SSID, aktywnego APRS-IS i wyłączonego Backup Digi. Szczegóły: [Network Failover](Network-Failover).

EN: Default OFF. Enable only after basic connectivity tests. Requires at least two SSIDs, active APRS-IS and backup digi disabled. See [Network Failover](Network-Failover).
