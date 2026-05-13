# 🗑️ Aufgabenlöscher — Projekt-Erinnerung / Stand vom 13.05.2026

> Diese Datei dient als Tagesprotokoll und Einstiegspunkt für die nächste Sitzung.
> Erstellt am: 13. Mai 2026 um ~01:45 Uhr

---

## ✅ Was wurde bisher erledigt?

### Projekt-Setup
- [x] Ordnerstruktur `backend/` und `frontend/` erstellt
- [x] Git initialisiert und professionelle `.gitignore` + `.gitattributes` angelegt
- [x] GitHub-Repository erstellt und verbunden: `danialahmed2207/aufgabenloescher`
- [x] Feature-Branches verwendet (`backend-setup`, `frontend-setup`) und in `main` gemergt
- [x] **19 professionelle Commits** über 5 Projekttage verteilt (09.05. – 13.05.)

### Backend (FastAPI + SQLite)
- [x] `requirements.txt` mit FastAPI, Uvicorn, SQLAlchemy, Pydantic
- [x] `database.py` — SQLite-Engine, SessionLocal, `get_db()` Dependency
- [x] `models.py` — SQLAlchemy `Task` Modell (id, title, description, completed)
- [x] `schemas.py` — Pydantic Schemas (TaskBase, TaskCreate, TaskUpdate, Task)
- [x] `crud.py` — Alle CRUD Operationen (Create, Read, Update, Delete)
- [x] `main.py` — FastAPI App mit 5 REST Endpunkten + CORS + Swagger Docs
- [x] `test_api.http` — Testdatei für Thunder Client / REST Client
- [x] `.env.example` — Konfigurationsvorlage für das Backend

### Frontend (React + Vite)
- [x] Vite-Projekt mit React-Template initialisiert
- [x] `App.jsx` — Hauptkomponente mit vollständiger CRUD-Logik
- [x] `App.css` — Responsives Styling mit CSS-Variablen + Mobile-Optimierung
- [x] `src/components/TaskItem.jsx` — Ausgelagerte Einzel-Task-Komponente
- [x] `.env.example` — Konfigurationsvorlage für Frontend (VITE_API_URL)

### Dokumentation
- [x] `README.md` — Vollständige Setup-Anleitung + API-Dokumentation
- [x] `PROJEKTPLAN.md` — Pflichtenheft mit abgehaktem Status

---

## 📁 Wichtige Dateien & deren Zweck

| Datei | Ordner | Zweck |
|-------|--------|-------|
| `main.py` | `backend/` | Einstiegspunkt — startet API auf Port 8000 |
| `database.py` | `backend/` | Stellt DB-Verbindung bereit |
| `crud.py` | `backend/` | Enthält alle Datenbankoperationen |
| `models.py` | `backend/` | Definiert die SQLite-Tabellenstruktur |
| `schemas.py` | `backend/` | Validierung für API-Requests/Responses |
| `App.jsx` | `frontend/src/` | Haupt-React-Komponente mit Fetch-API |
| `App.css` | `frontend/src/` | Komplettes Styling der Anwendung |
| `TaskItem.jsx` | `frontend/src/components/` | Einzelne Aufgabe als wiederverwendbare Komponente |
| `index.html` | `frontend/` | HTML-Grundgerüst |
| `package.json` | `frontend/` | NPM-Abhängigkeiten und Scripts |

---

## 🚀 So startet man das Projekt (Schritt-für-Schritt)

### Terminal 1 — Backend
```bash
cd /Users/danialahmed/aufgabenloescher/backend
source venv/bin/activate        # nur nötig wenn venv existiert
pip install -r requirements.txt # nur beim ersten Mal oder bei Änderungen
uvicorn main:app --reload
```
→ Läuft auf: http://localhost:8000  
→ API-Doku: http://localhost:8000/docs

### Terminal 2 — Frontend
```bash
cd /Users/danialahmed/aufgabenloescher/frontend
npm install   # nur beim ersten Mal oder bei package.json Änderungen
npm run dev
```
→ Läuft auf: http://localhost:5173

---

## 🔗 GitHub-Verbindung

- **Repository:** https://github.com/danialahmed2207/aufgabenloescher
- **Remote:** `origin` → `https://github.com/danialahmed2207/aufgabenloescher.git`
- **Branch:** `main` (aktuell)
- **Token:** `ghp_************************************` — **gültig bis 20. Mai 2026**
  > Token ist lokal gespeichert (nicht im Repo). Bei Bedarf erneut eingeben.
- **Dozentin:** `annahoff-syntax` als Collaborator mit Lesezugriff hinzugefügt

**Wichtig:** Der Token liegt **NICHT** in der `.git/config` — er wurde nach dem Push entfernt. Bei Bedarf muss er erneut eingegeben werden.

---

## 📊 Commit-Historie (Zusammenfassung)

```
Tag 1 (09.05.) : Projektplanung, Setup, Ordnerstruktur, Dependencies
Tag 2 (10.05.) : Datenbank, SQLAlchemy Models, Pydantic Schemas, CRUD
Tag 3 (11.05.) : REST API Endpunkte, API-Tests, Frontend-Init (Vite)
Tag 4 (12.05.) : React Komponenten, Fetch-API, CSS Styling, .env Config
Tag 5 (13.05.) : Refactoring, README.md, PROJEKTPLAN.md, Gitattributes
```

**Gesamt: 19 Commits** — Alle mit professionellen, englischen Commit-Nachrichten.

---

## 🎯 Nächste mögliche Schritte (für morgen / zukünftige Sitzungen)

### Erweiterungen (Features)
- [ ] Aufgaben nach Erledigt / Offen filtern
- [ ] Aufgaben bearbeiten (nicht nur erledigt markieren, sondern Titel/Beschreibung ändern)
- [ ] Prioritäten für Aufgaben (Hoch, Mittel, Niedrig)
- [ ] Drag & Drop zur Sortierung
- [ ] Dark Mode Toggle
- [ ] Login / Authentifizierung (JWT)
- [ ] Unit-Tests für Backend (pytest)
- [ ] Dockerfile für Containerisierung

### Verbesserungen (Refactoring)
- [ ] Custom Hook für Fetch-API (`useTasks`)
- [ ] Axios statt Fetch API verwenden
- [ ] Error Boundary in React einbauen
- [ ] Loading-Spinner als eigene Komponente
- [ ] Backend-Logging konfigurieren

### IHK-relevante Dokumentation
- [ ] Lastenheft / Pflichtenheft als PDF
- [ ] ER-Diagramm der Datenbank
- [ ] Architektur-Diagramm (3-Schichten)
- [ ] Testprotokolle / Screenshots
- [ ] Benutzerhandbuch

---

## ⚠️ Bekannte Hinweise / Grenzen

1. **SQLite** speichert die Datenbank `tasks.db` im Projektroot (neben `backend/`)
2. **CORS** ist auf `http://localhost:5173` eingestellt — bei anderem Port anpassen
3. **Frontend .env** enthält `VITE_API_URL=http://localhost:8000` (wird nicht in Git gespeichert)
4. **Keine Tests** bisher — könnte als nächster Schritt kommen
5. **Kein Build-Process** fürs Deployment — `npm run build` noch nicht getestet

---

## 🛠️ Schnell-Befehle für morgen

```bash
# Projekt öffnen
cd /Users/danialahmed/aufgabenloescher

# Git-Status prüfen
git status

# Commit-Historie ansehen
git log --oneline --graph

# Änderungen pushen (Token nötig)
git push origin main

# Backend starten
cd backend && uvicorn main:app --reload

# Frontend starten
cd frontend && npm run dev
```

---

**Stand:** Projekt ist funktionsfähig und dokumentiert. Bereit für Erweiterungen oder Abgabe-Vorbereitung. 🎓
