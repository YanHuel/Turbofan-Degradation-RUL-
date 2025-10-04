# Turbofan-Degradation-RUL-

## Einleitung
Prognose und Gesundheitsmanagement sind in der Industrie ein wichtiges Thema, um den Zustand von Anlagen vorherzusagen und so Ausfallzeiten und Ausfälle zu vermeiden. Dieses Machine-Learning-Projekt zielt darauf ab, einen Rahmen für die Vorhersage der verbleibenden Nutzungsdauer (Remaining Useful Lifetime - RUL) von Triebwerken basierend auf den gesamten Lebenszyklusdaten bereitzustellen. Verschiedene Regressions- und Klassifikationsmodelle werden eingesetzt, um die Lebensdauer zu bewerten. Die Daten entsprechen dem C-MAPSS-Datensatz der NASA.

## Datenbeschreibung
Triebwerke unterliegen während ihrer Lebensdauer Verschleiß, der sich direkt auf ihre Zuverlässigkeit und Leistung auswirkt. Die Simulation der Triebwerksdegradation wurde mit der Commercial Modular Aero-Propulsion System Simulation (C-MAPSS) durchgeführt. Vier verschiedene Sets wurden unter unterschiedlichen Kombinationen von Betriebsbedingungen und Fehlermodi simuliert. Dabei wurden mehrere Sensorkanäle aufgezeichnet, um die Fehlerentwicklung zu charakterisieren. Der Datensatz wurde vom NASA Ames Prognostics Center of Excellence (PCoE) bereitgestellt (https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/).

![Beispiel eines Strahltriebwerks](/assets/images/strahltriebwerk.jpg)



| Sensor | Beschreibung | Einheit |
| ------ | ------------ |-------- |
| T2 | Lüftereintrittstemperatur | °R |
| T24 | Niederdruckverdichter Austrittstemperatur | °R |
| T30 | Hochdruckverdichter Austrittstemperatur | °R |
| T50 |  Niederdruckturbine Austrittstemperatur | °R |
| P2 |  Lüftereintrittsdruck | psia |
| P15 |  Bypass-Kanaldruck | psia |
| P30 |  Hochdruckverdichter Austrittsdruck | psia |
| Nf |  Lüftergeschwindigkeit | rpm |
| Nc |  Kerngeschwindigkeit | rpm |
| epr | Motordruckverhältnis P50/P2 | - |
| Ps30 | Hochdruckverdichter statischer Ausdruckdruck | psia |
| phi | Kraftstoffdurchflussverhältnis zu Ps30 | pps/psia |
| NRf | korrigierte Lüftergeschwindigkeit | rpm |
| NRc | korrigierte Kerngeschwindigkeit | rpm |
| BPR | Bypass-Verhältnis | - |
| farB | Kraftstoff-Luft-Verhältnis des Brenners | - |
| htBleed | Enthalpie der Entlüftung | - |
| Nf_dmd | Gewünschte Lüftergeschwindigkeit | rpm |
| PCNfr_dmd | Gewünschte korrigierte Lüftergeschwindigkeit | rpm |
| W31 | Hochdruckturbine Kühlmittelentlüftung | lbm/s |
| W32 | Niederdruckturbine Kühlmittelentlüftung | lbm/s |
