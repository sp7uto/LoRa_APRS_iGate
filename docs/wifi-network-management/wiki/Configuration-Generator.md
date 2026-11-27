# Generator konfiguracji / Configuration Generator

[Standalone HTML / Samodzielny HTML](https://github.com/sp7uto/LoRa_APRS_iGate/blob/feature/wifi-network-management/docs/config-generator/index.html) — use Download raw file and open locally. / Pobierz surowy plik i otwórz lokalnie.

## PL
Pierwsza wersja obsługuje nowe konfiguracje bramki ESP32 RX-only (Heltec V3/V3.1). Podaj znak -10, własny passcode APRS-IS, pozycję, sieć Wi-Fi oraz profil radiowy odpowiadający trackerom. Zaawansowane ustawienia są opcjonalne; hasła Auto AP, WWW i OTA są generowane lokalnie i zapisane w JSON. Generator nie przechowuje ani nie wysyła danych. Pozycja i znak będą publiczne po uruchomieniu APRS-IS. Najpierw zachowaj kopię konfiguracji urządzenia, następnie w konfiguratorze wybierz Restore, wskaż JSON, sprawdź wszystkie ustawienia i dopiero wtedy Save. Nowy JSON zastępuje konfigurację, nie scala istniejącej. Nie wgrywaj go do produkcyjnej bramki przed testami. TX, RF beacon i digipeater są zawsze wyłączone.

## EN
Initial version creates new ESP32 RX-only iGate configurations for Heltec V3/V3.1. Enter callsign -10, your APRS-IS passcode, position, Wi-Fi and a matching radio profile. Advanced settings are optional; recovery AP, web and OTA passwords are generated locally and stored in the JSON. No storage or transmission of form data. Callsign and location become public when APRS-IS is used. Back up the device first, use Restore in its web UI, select the JSON, inspect all settings, then Save. This replaces the configuration rather than merging it. No production installation before hardware tests. TX, RF beacons and digipeater remain off.

GitHub Pages: planned URL [Configuration Generator](https://sp7uto.github.io/LoRa_APRS_iGate/config-generator/) — requires Pages activation (development branch, /docs). / Wymaga aktywacji Pages (gałąź rozwojowa, /docs).
