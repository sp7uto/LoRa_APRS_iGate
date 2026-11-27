# 🌐 Network Failover

## PL

Obecny kod próbuje sieci według ich kolejności, od góry. Brak prawidłowego adresu IP po próbie połączenia powoduje przejście do następnej sieci. Nieprawidłowy profil statyczny jest pomijany. Po nieudanych próbach Auto AP pozostaje mechanizmem awaryjnym, jeśli jest włączony. Zachowanie wymaga testów na sprzęcie.

**Planowane:** kontrola dostępności APRS-IS i Internetu, ograniczenie częstotliwości przełączeń, powrót do preferowanego AP. Obecnie uzyskanie adresu IP nie gwarantuje dostępności Internetu.

## EN

Profiles are tried in order, top first. Failure to obtain a valid IP causes the next profile to be attempted. Invalid static profiles are skipped. Auto AP is the fallback when enabled. Hardware validation remains required.

**Planned:** APRS-IS/Internet health checks, switching cooldown and preferred-network recovery. An IP address does not yet guarantee Internet reachability.
