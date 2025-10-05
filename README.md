# Turbofan-Engine-Degradation

## Einleitung
Prognose und Gesundheitsmanagement sind in der Industrie ein wichtiges Thema, um den Zustand von Anlagen vorherzusagen und so Ausfallzeiten und Ausfälle zu vermeiden. Dieses Machine-Learning-Projekt zielt darauf ab, einen Rahmen für die Vorhersage der verbleibenden Nutzungsdauer (Remaining Useful Lifetime - RUL) von Strahltriebwerken basierend auf den gesamten Lebenszyklusdaten bereitzustellen. Verschiedene Regressions- und Klassifikationsmodelle werden eingesetzt, um die Lebensdauer zu bewerten. Die Daten entsprechen dem C-MAPSS-Datensatz der NASA.

## Datenbeschreibung
Strahltriebwerke unterliegen während ihrer Lebensdauer Verschleiß, der sich direkt auf ihre Zuverlässigkeit und Leistung auswirkt. Die Simulation der Triebwerksdegradation wurde mit der Commercial Modular Aero-Propulsion System Simulation (C-MAPSS) durchgeführt. Vier verschiedene Sets wurden unter unterschiedlichen Kombinationen von Betriebsbedingungen und Fehlermodi simuliert. Dabei wurden mehrere Sensorkanäle aufgezeichnet, um die Fehlerentwicklung zu charakterisieren. Der Datensatz wurde vom NASA Ames Prognostics Center of Excellence (PCoE) bereitgestellt (https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/).

![Beispiel eines Strahltriebwerks](/assets/images/strahltriebwerk.jpg)

An den Triebwerken wurden insgesamt 21 Sensoren mit folgender Beschreibung angebracht:
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

Zur Veranschaulichung werden die ersten und letzten beiden Datenreihen des ersten Trainingsdatensatzes __*train_FD001.txt*__ vorgestellt. 
Zu beachten ist hier, dass __*time_in_cycles*__ für alle __*unit_number*__ unterschiedlich lang ist und die Zeit bis zum Ausfall des Triebwerks darstellt.

| Index | unit_number | time_in_cycles | setting 1 | setting 2 | setting 3 |    T2  |  T24  |    T30    |  T50   |  P2  |  P15  |   P30   |    Nf    |   Nc | epr  | Ps30  |   phi   |   NRf    |  NRc  |   BPR | farB | htBleed | Nf_dmd | PCNfR_dmd  |  W31   |   W32 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1  | 1 | -0.0007 | -0.0004 | 100.0 | 518.67 | 641.82 | 1589.70 | 1400.60  | 14.62 | 21.61 | 554.36 | 2388.06 | 9046.19 | 1.3 | 47.47 | 521.66 | 2388.02 | 8138.62 | 8.4195 | 0.03 | 392 | 2388 | 100.0 | 39.06 | 23.4190 |
| 1 | 1  | 2 | 0.0019 | -0.0003 | 100.0 | 518.67 | 642.15 | 1591.82 | 1403.14 | 14.62  | 21.61 | 553.75 | 2388.04 | 9044.07 | 1.3 | 47.49 | 522.28 | 2388.07 | 8131.49 | 8.4318 | 0.03  | 392 | 2388 | 100.0 | 39.00|  23.4236 |
| 20629 | 100 | 199 | -0.0011 | 0.0003 | 100.0 | 518.67 | 643.23 | 1605.26 | 1426.53 | 14.62 | 21.61 | 550.68 | 2388.25 | 9073.72 | 1.3 | 48.39 | 519.67 | 2388.23 | 8139.29 | 8.5389 | 0.03 | 395  | 2388 | 100.0 | 38.29 | 23.0640 |
| 20630 | 100 | 200 | -0.0032 | -0.0005 | 100.0 | 518.67 | 643.85 | 1600.38 | 1432.14 | 14.62 | 21.61 | 550.79 | 2388.26 | 9061.48 | 1.3 | 48.20 | 519.30 | 2388.26 | 8137.33 | 8.5036 | 0.03 | 396  | 2388 | 100.0 | 38.37 | 23.0522 |


## Datenvisualisierung
Im folgenden Bild ist erkennbar, dass die meisten Triebwerke um die 200 Zyklen vor Ausfall besitzen.

![Verteilung alle Lebenszyklen](/assets/images/VerteilungLeben.png)



