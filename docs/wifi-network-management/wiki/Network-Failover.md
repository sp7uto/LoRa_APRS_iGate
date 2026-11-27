# 🌐 Network Failover

## PL
Domyślnie wyłączona opcja Experimental APRS-IS WiFi failover w Connectivity. Włącz dopiero po testach zwykłej łączności. Przy co najmniej dwóch zapisanych SSID, aktywnym APRS-IS, normalnym trybie i wyłączonym Backup Digi, monitorowane są potwierdzona autoryzacja oraz ostatnia niepusta linia z serwera. Po 90 s ciszy sesja jest zamykana; po 3 min niezdrowego stanu kolejna sieć jest próbowana w kolejności cyklicznej. Minimum 5 min między przełączeniami. Jeżeli inne AP nie działają, próbuje wrócić do poprzedniego; przy całkowitej utracie Wi-Fi uruchamia Auto AP (jeśli włączony). Nie wraca samoczynnie do preferowanego AP, jeśli bieżący działa. Nie sprawdza publicznych serwisów ani nie rozróżnia awarii serwera od awarii Internetu. Przy błędnym passcode APRS-IS jest wyłączany jak w upstream; failover wtedy nie działa. Nie zmienia TX ani digi.

## EN
Opt-in Experimental APRS-IS WiFi failover under Connectivity (off by default). With at least two configured SSIDs, APRS-IS enabled, normal mode and backup digi disabled, health requires verified authentication and recent nonempty server data. A silent session closes after 90 s; after 3 minutes of unhealthy state the next profile is tried in cyclic order. Minimum 5 minutes between switches. If alternatives fail, the previous AP is retried; Auto AP is used on complete Wi-Fi failure if enabled. No automatic failback while healthy. No public Internet probes; upstream server failure and Internet failure cannot be distinguished. Invalid passcode disables APRS-IS as upstream, so no failover. No TX/digi changes.

## Status
Experimental code; CI and hardware tests required. / Kod eksperymentalny; wymagane testy CI i sprzętowe.
