# Projektanalyse – JobTracker

## 1. Projektname

JobTracker – Bewerbungsmanager

## 2. Ausgangssituation

Bei vielen Bewerbungen ist es schwer, den Überblick zu behalten. Man bewirbt sich bei mehreren Firmen, bekommt verschiedene Rückmeldungen und hat manchmal Gespräche, Aufgaben oder Fristen. Wenn diese Informationen nur in E-Mails, Notizen oder Excel-Dateien stehen, können wichtige Termine oder Statusänderungen verloren gehen.

## 3. Problem

Der Benutzer braucht eine einfache Anwendung, um Bewerbungen zentral zu speichern und den aktuellen Status jeder Bewerbung schnell zu sehen.

## 4. Ziel des Projekts

Ziel ist die Entwicklung einer Webanwendung, mit der Bewerbungen angelegt, bearbeitet, gelöscht, gefiltert und nach Status verfolgt werden können.

Die Anwendung soll später auch Statistiken, Notizen, Termine und Dateien unterstützen.

## 5. Zielgruppe

Die Anwendung ist für Personen gedacht, die sich aktiv bewerben und ihre Bewerbungen übersichtlich verwalten möchten.

## 6. Hauptfunktionen für die erste Version

Die erste Version soll folgende Funktionen enthalten:

* Bewerbung anlegen
* Bewerbung anzeigen
* Bewerbung bearbeiten
* Bewerbung löschen
* Status einer Bewerbung speichern
* Bewerbungen nach Status filtern
* einfache Übersicht aller Bewerbungen anzeigen

## 7. Mögliche Felder einer Bewerbung

Eine Bewerbung soll mindestens folgende Felder haben:

* Firma
* Stellenbezeichnung
* Ort
* Bewerbungslink
* Quelle der Stellenanzeige
* Bewerbungsdatum
* Status
* Notiz
* Erstellungsdatum
* Änderungsdatum

## 8. Statuswerte

Folgende Statuswerte werden für den Anfang verwendet:

* geplant
* beworben
* gespräch
* aufgabe
* absage
* zusage

## 9. Muss-Anforderungen

Die Anwendung muss Bewerbungen speichern können.

Die Anwendung muss Bewerbungen anzeigen können.

Die Anwendung muss Bewerbungen bearbeiten und löschen können.

Die Anwendung muss den Status einer Bewerbung speichern können.

Die Anwendung muss eine einfache Filterung nach Status ermöglichen.

## 10. Kann-Anforderungen für spätere Versionen

Später können folgende Funktionen ergänzt werden:

* Benutzerregistrierung und Login
* Dashboard mit Statistiken
* Datei-Upload für Lebenslauf und Anschreiben
* Erinnerungen für Gesprächstermine
* Export als CSV oder PDF
* REST API
* Vue.js Frontend
* FastAPI-Version als Vergleich

## 11. Akzeptanzkriterien für MVP

Das MVP gilt als fertig, wenn:

* eine Bewerbung über die Weboberfläche angelegt werden kann
* alle Bewerbungen in einer Liste angezeigt werden
* eine Bewerbung bearbeitet werden kann
* eine Bewerbung gelöscht werden kann
* der Status geändert werden kann
* Bewerbungen nach Status gefiltert werden können
* mindestens einfache Tests vorhanden sind
* das Projekt über Git sauber versioniert ist
* eine README-Datei vorhanden ist

## 12. Technische Entscheidung für Version 1

Version 1 wird als Django-Webanwendung umgesetzt.

Für den Anfang wird Django mit HTML-Templates verwendet. Dadurch kann zuerst das Backend, das Datenmodell und die Grundlogik sauber gelernt werden.

Vue.js und FastAPI werden nicht am Anfang eingebaut, sondern später als Erweiterung.
