# Erklärung des Level-System Discord Bots
Dieser Bot ist ein Discord-Bot, der ein Level-System für Benutzer implementiert. Er verfolgt die Aktivität der Benutzer basierend auf der Anzahl der gesendeten Nachrichten und vergibt entsprechend Erfahrungspunkte (XP), um die Benutzer zu leveln. Hier ist eine detaillierte Erklärung, wie der Bot funktioniert:

# Funktionen und Merkmale
Bot-Initialisierung
Der Bot wird mit den benötigten Berechtigungen (Intents) initialisiert, um Nachrichten und Mitgliederinformationen verarbeiten zu können. Beim Starten des Bots werden alle Erweiterungen (Cogs) im Verzeichnis "cogs" geladen.

# Level-System
1. Der Kern des Level-Systems wird in einer eigenen Klasse (levelSystem) implementiert. Diese Klasse enthält Methoden zum Verwalten und Verfolgen von Benutzeraktivitäten:
  - XP und Level Berechnung: Die Methode get_level berechnet das Level eines Benutzers basierend auf den gesammelten XP. Der Erfahrungsbedarf steigt exponentiell mit jedem Level.
  - Datenbank Initialisierung: Beim Start des Bots wird überprüft, ob die benötigte SQLite-Datenbank und die Tabelle für Benutzer existieren. Falls nicht, werden sie erstellt.
  - Benutzerüberprüfung: Die Methode check_user stellt sicher, dass jeder Benutzer in der Datenbank vorhanden ist, indem er einen Eintrag hinzufügt, wenn der Benutzer noch nicht existiert.
   -XP Verwaltung: Die Methode on_message verarbeitet jede gesendete Nachricht. Sie aktualisiert die XP und die Anzahl der Nachrichten für den Benutzer und überprüft, ob der Benutzer ein neues Level erreicht hat.

Benutzerbefehle
Der Bot bietet verschiedene Slash-Befehle für die Benutzerinteraktion:

/rank: Zeigt die aktuellen XP und das Level eines angegebenen Benutzers an.
/messages: Zeigt die Anzahl der gesendeten Nachrichten eines angegebenen Benutzers an.
/leaderboard: Zeigt die Top 10 Benutzer mit den meisten XP auf dem Server an.
Datenbank
Die Datenbank speichert die Benutzerinformationen, einschließlich der Anzahl der gesendeten Nachrichten und der gesammelten XP. Die Datenbank wird bei jedem Ereignis, das die Benutzeraktivität betrifft, aktualisiert.

Zusammenfassung
Dieser Level-System Discord Bot bietet eine unterhaltsame Möglichkeit, die Aktivität der Benutzer auf einem Discord-Server zu verfolgen und zu belohnen. Benutzer können ihre Fortschritte und den Wettbewerb mit anderen über verschiedene Befehle verfolgen. Die Verwendung von SQLite für die Datenbank und die Implementierung der Level-Logik ermöglichen eine effiziente und skalierbare Lösung.
