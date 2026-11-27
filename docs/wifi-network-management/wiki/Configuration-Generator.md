# Generator konfiguracji / Configuration Generator

[**Uruchom generator / Launch configuration generator**](https://sp7uto.github.io/LoRa_APRS_iGate/config-generator/) — GitHub Pages (requires activation / wymaga aktywacji).

[Standalone HTML / Samodzielny HTML](https://github.com/sp7uto/LoRa_APRS_iGate/blob/feature/wifi-network-management/docs/config-generator/index.html) — use Download raw file and open locally. / Pobierz surowy plik i otwórz lokalnie.

## PL
Tryb nowej konfiguracji obsługuje bramki ESP32 RX-only (Heltec V3/V3.1). Podaj znak -10, własny passcode APRS-IS, pozycję, sieć Wi-Fi oraz profil radiowy odpowiadający trackerom. Zaawansowane ustawienia są opcjonalne; hasła Auto AP, WWW i OTA są generowane lokalnie i zapisane w JSON. Generator nie przechowuje ani nie wysyła danych. Pozycja i znak będą publiczne po uruchomieniu APRS-IS. Najpierw zachowaj kopię konfiguracji urządzenia, następnie w konfiguratorze wybierz Restore, wskaż JSON, sprawdź wszystkie ustawienia i dopiero wtedy Save. W trybie nowej konfiguracji JSON zastępuje konfigurację; do zachowania istniejących wartości użyj trybu importu opisanego niżej. Nie wgrywaj go do produkcyjnej bramki przed testami. W trybie nowej konfiguracji TX, RF beacon i digipeater są wyłączone.

## EN
New configuration mode creates ESP32 RX-only iGate configurations for Heltec V3/V3.1. Enter callsign -10, your APRS-IS passcode, position, Wi-Fi and a matching radio profile. Advanced settings are optional; recovery AP, web and OTA passwords are generated locally and stored in the JSON. No storage or transmission of form data. Callsign and location become public when APRS-IS is used. Back up the device first, use Restore in its web UI, select the JSON, inspect all settings, then Save. New configuration mode replaces the configuration; to preserve existing settings use import below. No production installation before hardware tests. In new configuration mode TX, RF beacons and digipeater remain off.

GitHub Pages: planned URL [Configuration Generator](https://sp7uto.github.io/LoRa_APRS_iGate/config-generator/) — requires Pages activation (development branch, /docs). / Wymaga aktywacji Pages (gałąź rozwojowa, /docs).

## Import i edycja kopii / Import and edit a backup

PL: Wczytaj istniejący JSON przyciskiem **Wczytaj istniejący JSON**. Oryginał i niezmienione pola pozostają zachowane, także hasła i nieznane klucze. Przycisk uzupełniania Wi-Fi dodaje tylko brakujące pola DHCP/static i APRS-IS failover (bez nadpisania istniejących). Można zmieniać kolejność AP, parametry radiowe i pozostałe znane ustawienia; brakujące pola są oznaczone. Profile RX-only, RX/TX, WIDE1, WIDE2, samodzielny WIDE1 i awaryjny digi są opcjonalne i wymagają świadomego zastosowania. Przed eksportem sprawdź różnice (hasła zamaskowane). Zmiana ustawień nadawania wymaga potwierdzenia. Eksport to osobny plik JSON; nie zapisuje nic na urządzeniu. Nieznane klucze zachowuje generator, ale firmware może je ignorować lub usunąć po zapisaniu. Nie importować pliku innego urządzenia, np. trackera lub RP2350 Ethernet. Test na fizycznym urządzeniu nadal wymagany.

EN: Import an existing iGate JSON with **Import existing JSON**. Original and untouched values, passwords and unknown keys remain intact. Wi-Fi upgrade adds missing DHCP/static and APRS-IS failover keys only. Edit priority, radio and other known settings; missing fields are marked. Optional RX-only, RX/TX, WIDE1, WIDE2, standalone WIDE1 and backup digi profiles require explicit application. Review masked differences and confirm RF changes before export. Export is a separate JSON, not a device write. Unknown keys are preserved by the generator, but firmware may discard them on Save. Tracker and RP2350 Ethernet backups are unsupported. Hardware testing still required.

## Współrzędne / Coordinates

W obu trybach / Both modes: DD (decimal degrees), DDM (degrees and decimal minutes), DMS (degrees, minutes, seconds) and APRS compact with hemisphere. Dot or comma, N/S/E/W prefix or suffix, signed decimal degrees, spaces or colons. / Kropka lub przecinek, kierunek przed lub po liczbie, znak +/−, spacje lub dwukropki.

| Format | Latitude | Longitude |
| --- | --- | --- |
| DD | 51.590333 | 18.737 |
| DD with comma | 51,590333 | 18,737 |
| DDM | 51°35.42′ N | 18°44.22′ E |
| DMS | 51°35′25.2″ N | 18°44′13.2″ E |
| APRS | 5135.42N | 01844.22E |

All edited coordinates are exported as numeric WGS84 decimal degrees; S/W negative. Invalid ranges, minutes or seconds ≥60, conflicting sign/direction or wrong hemisphere are rejected. Untouched imported coordinates are preserved. / Eksport edytowanych współrzędnych w liczbowych stopniach dziesiętnych WGS84; S/W ujemne. Błędne zakresy, minuty/sekundy ≥60 i sprzeczne kierunki odrzucane. Nieedytowane współrzędne importu pozostają bez zmian.
