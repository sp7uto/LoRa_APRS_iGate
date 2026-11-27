# Testy i odzyskiwanie / Tests and recovery

| Test / Próba | Expected / Oczekiwany wynik |
|---|---|
| Legacy JSON | DHCP by default |
| DHCP AP | Valid lease and APRS-IS |
| No DHCP, static profile | Configured IP and APRS-IS |
| No DHCP, DHCP profile | Next configured AP |
| Static → DHCP | New lease, no stale IP |
| Wrong static subnet | Rejected profile |
| Reorder/delete profile | Persisted order and settings |
| All APs fail | Auto AP if enabled |
| Reboot / restore | Correct persistent values |

PL: Przed testami zachowaj kopię JSON i oficjalny firmware. Nie zmieniaj produkcyjnej bramki. Na stanowisku testowym utrzymuj TX wyłączony. W razie problemu wróć przez USB do oficjalnego obrazu i przywróć konfigurację. Test walidatora nie zastępuje kompilacji ani testu sprzętowego.

EN: Save JSON and the official firmware before testing. Use a separate test unit, with TX disabled. If needed, restore official firmware via USB and reload configuration. Validator tests are not a substitute for compilation and hardware verification.
