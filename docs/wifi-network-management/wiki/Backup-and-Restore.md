# 🗄️ Backup & Restore

## 🇵🇱 Przed testem jedynego Helteca V3.1

1. Zachowaj prywatny eksport JSON, wersję oficjalnego firmware i dostęp USB. Nie publikuj kopii.
2. Odłącz zewnętrzne zasilanie, pozostaw antenę i podłącz USB. Zamknij terminale zajmujące port COM. Sprawdź port w Menedżerze urządzeń.
3. W PowerShell z działającym Python i esptool 5.x wykonaj polecenia poniżej. Zastąp COM6 rzeczywistym portem. Odczyt flash_id nie zapisuje pamięci. Kontynuuj tylko jeśli rozpoznano ESP32-S3 z 8 MB flash; w innym przypadku STOP.
4. Wykonaj dwa pełne odczyty i porównaj SHA256. W razie różnicy nie aktualizuj. Kopie zawierają hasła i inne dane prywatne.

## 🇬🇧 Before testing the only Heltec V3.1

Export private JSON, retain official firmware, keep USB access. Close applications using the serial port and check its number. The following commands are for esptool 5.x and PowerShell. Replace COM6. Only continue if flash_id confirms ESP32-S3 and 8 MB flash. Read twice and compare hashes; stop on any discrepancy. Store both full flash backups privately.

```powershell
$ErrorActionPreference = "Stop"
$port = "COM6"
$dir = Join-Path $HOME ("igate-backup-" + (Get-Date -Format "yyyyMMdd-HHmmss"))
New-Item -ItemType Directory -Path $dir | Out-Null
Set-Location $dir
python -m esptool version
if ($LASTEXITCODE -ne 0) { throw "esptool unavailable" }
python -m esptool --chip esp32s3 --port $port flash-id
if ($LASTEXITCODE -ne 0) { throw "Flash detection failed" }
```

**STOP unless detected flash is exactly 8 MB. / Kontynuuj tylko przy 8 MB.**

```powershell
python -m esptool --chip esp32s3 --port $port --baud 115200 read-flash 0x0 0x800000 original-a.bin
if ($LASTEXITCODE -ne 0) { throw "Read A failed" }
python -m esptool --chip esp32s3 --port $port --baud 115200 read-flash 0x0 0x800000 original-b.bin
if ($LASTEXITCODE -ne 0) { throw "Read B failed" }
if ((Get-Item original-a.bin).Length -ne 8388608 -or (Get-Item original-b.bin).Length -ne 8388608) { throw "Wrong backup size" }
$a = (Get-FileHash original-a.bin -Algorithm SHA256).Hash
$b = (Get-FileHash original-b.bin -Algorithm SHA256).Hash
if ($a -ne $b) { throw "Backup hashes differ" }
$a | Set-Content original-sha256.txt
Write-Host "BACKUP VERIFIED: $a"
```

## Rollback / Przywracanie awaryjne

PL: Tylko dla tego samego fizycznego urządzenia, jeżeli test się nie powiedzie. W trybie USB bootloader sprawdź SHA256 i rozmiar oryginalnej kopii. Jeśli urządzenie ma włączone szyfrowanie flash lub secure boot, nie wykonuj przywracania bez sprawdzenia ograniczeń. Polecenie zapisuje całą pamięć, nadpisując aktualny firmware i konfigurację. Nie uruchamiaj erase-flash jako kroku przygotowawczego. Po zapisie sprawdź konfigurację, RX-only, APRS-IS i Auto AP.

EN: Only for the same physical device, if the experiment fails. Verify the saved hash and size in USB bootloader mode. Do not proceed on secure boot/flash encryption without checking restrictions. This overwrites the whole flash, including configuration. Do not pre-erase. Verify configuration, RX-only, APRS-IS and Auto AP afterward.

```powershell
# Run in the original backup directory. / W katalogu oryginalnej kopii.
$expected = (Get-Content original-sha256.txt -Raw).Trim()
if ((Get-Item original-a.bin).Length -ne 8388608) { throw "Wrong size" }
if ((Get-FileHash original-a.bin -Algorithm SHA256).Hash -ne $expected) { throw "Hash mismatch" }
python -m esptool --chip esp32s3 --port $port --baud 115200 write-flash 0x0 original-a.bin
if ($LASTEXITCODE -ne 0) { throw "Restore failed" }
python -m esptool --chip esp32s3 --port $port --baud 115200 verify-flash 0x0 original-a.bin
if ($LASTEXITCODE -ne 0) { throw "Verification failed" }
```

This is a proposed test procedure, not a verified recovery on SP7UTO-10. / Procedura nie została jeszcze sprawdzona na SP7UTO-10.
