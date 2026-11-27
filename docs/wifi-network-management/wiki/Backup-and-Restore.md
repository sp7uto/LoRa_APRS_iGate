# 🗄️ Backup & Restore

## PL

1. Wyeksportuj JSON przez konfigurator przed zmianami. Przechowuj go prywatnie.
2. Zachowaj oficjalny obraz firmware dla dokładnej wersji płytki.
3. Starszy JSON bez pola dhcp używa domyślnie DHCP. Nowe pola statycznego IPv4 są rozszerzeniem formatu.
4. W razie utraty sieci spróbuj Auto AP, jeśli był aktywny. Jeśli nie działa, użyj USB i oficjalnej procedury odzyskania, a następnie przywróć wcześniejszy JSON.

## EN

Export a private JSON backup and retain the official firmware for the exact board. Legacy JSON without dhcp defaults to DHCP. New static IPv4 fields extend the schema. If the network is lost, try Auto AP when enabled, otherwise recover via USB using the official procedure and restore your previous JSON. Do not assume a downgrade retains every new field.
