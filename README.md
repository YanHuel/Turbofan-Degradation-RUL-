# Turbofan-Degradation-RUL-

## Einleitung
Prognose und Gesundheitsmanagement sind in der Industrie ein wichtiges Thema, um den Zustand von Anlagen vorherzusagen und so Ausfallzeiten und Ausfälle zu vermeiden. Dieses Machine-Learning-Projekt zielt darauf ab, einen Rahmen für die Vorhersage der verbleibenden Nutzungsdauer (Remaining Useful Lifetime - RUL) von Triebwerken basierend auf den gesamten Lebenszyklusdaten bereitzustellen. Verschiedene Regressions- und Klassifikationsmodelle werden eingesetzt, um die Lebensdauer zu bewerten. Die Daten entsprechen dem C-MAPSS-Datensatz der NASA.

## Datenbeschreibung
Triebwerke unterliegen während ihrer Lebensdauer Verschleiß, der sich direkt auf ihre Zuverlässigkeit und Leistung auswirkt. Die Simulation der Triebwerksdegradation wurde mit der Commercial Modular Aero-Propulsion System Simulation (C-MAPSS) durchgeführt. Vier verschiedene Sets wurden unter unterschiedlichen Kombinationen von Betriebsbedingungen und Fehlermodi simuliert. Dabei wurden mehrere Sensorkanäle aufgezeichnet, um die Fehlerentwicklung zu charakterisieren. Der Datensatz wurde vom NASA Ames Prognostics Center of Excellence (PCoE) bereitgestellt (https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/).

![Beispiel eines Strahltriebwerks](/assets/images/strahltriebwerk.jpg)


Beschreibung der 21 Sensoren des Datensatzes
- Sensor 1:  Lüftereintrittstemperatur [°R]
- Sensor 2:  Niederdruckverdichter Ausgangstemperatur [°R]
- Sensor 3:  Hochdruckverdichter Ausgangstemperatur [°R]
