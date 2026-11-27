# 💾 Instalacja / Installation

## PL

Nie instaluj wersji eksperymentalnej na działającej bramce przed pomyślnymi testami. Zachowaj oficjalny firmware, kopię JSON i dostęp USB. Używaj oddzielnego egzemplarza testowego z TX wyłączonym. Artefakt CI jest obrazem aplikacji (OTA), nie pełnym obrazem flash. Nie wgrywaj go pod offset 0x0. Instalator przeglądarkowy i wydanie stabilne nie są jeszcze dostępne.

## EN

Do not install the experimental branch on a production gateway before successful testing. Keep the official firmware, JSON backup and USB access. Use a separate test device with TX disabled. The CI artifact is an application/OTA image, not a full flash image; do not flash it at offset 0x0. Web installer and stable release are not yet available.

[Build status](https://github.com/sp7uto/LoRa_APRS_iGate/actions) · [Recovery](Backup-and-Restore)

## Experimental package / Pakiet eksperymentalny

CI builds an application OTA image and (when packaging succeeds) a factory image with default SPIFFS, using upstream ESP32-S3 offsets. SHA256SUMS.txt and COMMIT.txt identify the build. Factory image starts at 0x0000 and overwrites existing configuration; OTA is for the official compatible web updater only. Do not install before verifying backup and actual board/partition compatibility.

CI tworzy obraz OTA oraz (po udanym pakowaniu) obraz fabryczny z domyślnym SPIFFS według układu upstream ESP32-S3. SHA256SUMS.txt i COMMIT.txt identyfikują kompilację. Obraz fabryczny nadpisuje konfigurację; OTA wyłącznie przez zgodny aktualizator WWW. Instalator Pages nie jest jeszcze wdrożony. Przed instalacją sprawdź kopie, model płytki i zgodność partycji.
