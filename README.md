# daVinci
DaVinci Bazar Projekt

Constest Website: https://codingdavinci.de/daten/der-bazar-ein-illustriertes-modejournal-aus-dem-19-jh-mit-zahlreichen-beilagen-schnittmuster

Project Website: https://hackdash.org/projects/616401766d202d739f69c8b3


Räumliche Inszenierung mit den visuellen Inhalten der Zeitschrift.

Die gesammelten Ausgaben der Zeitschrift „Der Bazar“ beinhalten einen großen Schatz an Abbildungen, die Moden, Möbel, Muster und Maschinen des 19. Jh zeigen. Diese Abbildungen aus den PDFs zu extrahieren, mit Schlagworten zu versehen und somit den Datenschatz nutzbar zu machen soll Aufgabe dieses Projektes sein.

Die so gewonnenen Daten sollen dann dazu verwendet werden, über Projektionen eine räumliche Inszenierung zu erschaffen, die die Bilderwelten der zweiten Hälfte des 19. Jh aufleben lässt.

Verknüpfung der gewonnenen Daten mit realen Objekten aus den anderen Datensets von CDV:

Diese (projizierten) Bilderwelten des 19. Jh können beispielsweise mit einer Ausstellung der Uhren von Schloss Benrath oder mit Objekten (Schmuck) des MAKK kombiniert werden. So können die ausgestellten Objekte mit Kontextinformationen der Epoche gezeigt und in Bilderwelten der jeweiligen Zeit eingebettet werden.

Extraktion

Extraktion, Kategorisierung, Segmentierung der visuellen Elemente in den vorhandenen Daten (PDFs) durch Mustererkennung und Machine Learning.
Ergebnis soll eine Datenbank sein, bei der die einzelnen Elemente der PDF-Scans extrahiert, frei gestellt und mit Metadaten versehen sind. (Die gewonnen und angereicherten Daten können, falls gewünscht, in die Datenbank der Universitäts- und Landesbibliothek Düsseldorf übernommen werden. )

Beispiele Metadaten:

-Kategorie: (Bildszene, Mode, Möbel, Handarbeitsmuster, Schnittmuster, Technisches Gerät, Noten, Werbeanzeige ....)
-Datum, Ausgabe, Seitennummer: durch OCR der Kopf-/Fußzeilen und Bildunterschriften.

Anwendung

Die gewonnenen Daten sollen über eine GameEngine visualisiert werden.
Projektionen der Inhalte aus den Zeitschriften in eine gebaute Kulisse.
Angelehnt an die 2,5 D Ästhetik der Papiertheater des 19. Jahrhunderts.
Räumliches Erlebbarmachen der Bilder, Gegenstände und Musterwelten der einzelnen Ausgaben von „Bazar".
Möglichkeit der Interaktion/Immersion.
hackdash.org

Requirements:
- Python3 installed
- Linux System or Power Shell access (Win 11 native command line?)
