# 🗑️ Aufgabenlöscher — Projekt-Erinnerung / Aktueller Stand

> Diese Datei dient als Tagesprotokoll und Einstiegspunkt für die nächste Sitzung.
> Zuletzt aktualisiert: 13. Mai 2026

---

## ✅ WAS WURDE BISHER ERLEDIGT?

### Lokales Projekt (Entwicklung)
- [x] Ordnerstruktur `backend/` und `frontend/` erstellt
- [x] Git initialisiert und professionelle `.gitignore` + `.gitattributes` angelegt
- [x] GitHub-Repository verbunden: `danialahmed2207/TaskFlow-Fullstack-Aufgabenmanager`
- [x] Feature-Branches verwendet (`backend-setup`, `frontend-setup`) und in `main` gemergt
- [x] **23 professionelle Commits** über 5 Projekttage verteilt (09.05. – 13.05.)

### Backend (FastAPI + SQLite)
- [x] `requirements.txt` mit FastAPI, Uvicorn, SQLAlchemy, Pydantic
- [x] `database.py` — SQLite-Engine, SessionLocal, `get_db()` Dependency
- [x] `models.py` — SQLAlchemy `Task` Modell
- [x] `schemas.py` — Pydantic Schemas (TaskBase, TaskCreate, TaskUpdate, Task)
- [x] `crud.py` — Alle CRUD Operationen
- [x] `main.py` — FastAPI App mit 5 REST Endpunkten + CORS + Swagger Docs
- [x] `test_api.http` — Testdatei für Thunder Client / REST Client
- [x] `.env.example` — Konfigurationsvorlage

### Frontend (React + Vite)
- [x] Vite-Projekt mit React-Template initialisiert
- [x] `App.jsx` — Hauptkomponente mit vollständiger CRUD-Logik
- [x] `App.css` — Responsives Styling mit CSS-Variablen + Mobile-Optimierung
- [x] `src/components/TaskItem.jsx` — Ausgelagerte Einzel-Task-Komponente
- [x] `.env.example` — Konfigurationsvorlage

### Dokumentation
- [x] `README.md` — Vollständige Setup-Anleitung + API-Dokumentation
- [x] `PROJEKTPLAN.md` — Pflichtenheft mit abgehaktem Status
- [x] `dokumentation/TAG-02-PROTOKOLL.md` — Tagesprotokoll Tag 2 (10.05.)
- [x] `dokumentation/TAG-05-PROTOKOLL.md` — Tagesprotokoll Tag 5 (13.05.)
- [x] `dokumentation/TAG-05-AWS-DEPLOYMENT.md` — AWS Deployment Protokoll
- [x] `dokumentation/AWS-DEPLOYMENT.md` — AWS Deployment Anleitung

---

## ☁️ AWS DEPLOYMENT (ERLEDIGT AM 13.05.)

### AWS-Ressourcen

| Ressource | ID / Name |
|-----------|-----------|
| **VPC** | `vpc-08771a5f5401d5547` |
| **EC2 Instance** | `i-08a82ffebd6802307` |
| **Security Group** | `sg-05c21ee1d31d3f105` |
| **SSH Key Pair** | `aufgabenloescher-key` |
| **AWS Account** | `579320645741` (Techstarter Sandbox) |

### Server-Konfiguration
- **OS:** Ubuntu 22.04 LTS
- **Webserver:** Nginx (Ports 80 + 443)
- **Backend:** FastAPI + Uvicorn (Port 8000, intern)
- **Datenbank:** SQLite (`tasks.db`)
- **SSL:** Selbst-signiertes Zertifikat (für Demo)
- **Monitoring:** Cronjob alle 5 Minuten (`/status.html`)
- **Auto-Deploy:** Skript unter `/usr/local/bin/deploy-aufgabenloescher`

### Wichtige Hinweise
- ⚠️ Die EC2-Instanz ist aktuell **GESTOPPT** (keine laufenden Kosten)
- ⚠️ Die öffentliche IP ändert sich bei jedem Neustart!
- 💡 Für feste IP: Elastic IP erstellen und zuweisen

---

## 📁 Wichtige Dateien & deren Zweck

| Datei | Ordner | Zweck |
|-------|--------|-------|
| `main.py` | `backend/` | FastAPI Einstiegspunkt |
| `database.py` | `backend/` | SQLite Verbindung |
| `crud.py` | `backend/` | Datenbankoperationen |
| `models.py` | `backend/` | Tabellenstruktur |
| `schemas.py` | `backend/` | API-Validierung |
| `server.py` | `backend/` | Flask Demo-Backend (Python 3.14 Fallback) |
| `s3-policy.json` | `backend/` | S3 Bucket Policy Template |
| `App.jsx` | `frontend/src/` | Haupt-React-Komponente |
| `App.css` | `frontend/src/` | Styling |
| `TaskItem.jsx` | `frontend/src/components/` | Einzelne Aufgabe |

---

## 🚀 SO STARTEST DU DAS PROJEKT (LOKAL)

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

## ☁️ SO STARTEST DU DIE AWS-INSTANZ WIEDER

### 1. Instanz starten
```bash
aws ec2 start-instances --instance-ids i-08a82ffebd6802307 --profile Danial --region eu-central-1
```

### 2. Neue öffentliche IP abrufen
```bash
aws ec2 describe-instances \
  --instance-ids i-08a82ffebd6802307 \
  --query 'Reservations[0].Instances[0].PublicIpAddress' \
  --output text \
  --profile Danial \
  --region eu-central-1
```

### 3. Services prüfen (nach dem Start)
```bash
ssh -i /tmp/aufgabenloescher-key.pem ubuntu@NEUE-IP
sudo systemctl status aufgabenloescher   # Backend
sudo systemctl status nginx               # Webserver
sudo /usr/local/bin/update-monitor        # Monitoring aktualisieren
```

### 4. Deploy-Skript ausführen (bei Code-Änderungen)
```bash
ssh -i /tmp/aufgabenloescher-key.pem ubuntu@NEUE-IP 'deploy-aufgabenloescher'
```

---

## 🔗 GitHub-Verbindung

- **Repository:** https://github.com/danialahmed2207/TaskFlow-Fullstack-Aufgabenmanager
- **Remote:** `origin` → `https://github.com/danialahmed2207/TaskFlow-Fullstack-Aufgabenmanager.git`
- **Branch:** `main` (aktuell)
- **Token:** `ghp_************************************` — **gültig bis 20. Mai 2026**
  > Token ist lokal gespeichert (nicht im Repo). Bei Bedarf erneut eingeben.
- **Dozentin:** `annahoff-syntax` als Collaborator mit Lesezugriff

**Wichtig:** Der Token liegt **NICHT** in der `.git/config` — er wurde nach dem Push entfernt. Bei Bedarf muss er erneut eingegeben werden.

---

## 📊 Commit-Historie (Zusammenfassung)

```
Tag 1 (09.05.) : Projektplanung, Setup, Ordnerstruktur, Dependencies
Tag 2 (10.05.) : Datenbank, SQLAlchemy Models, Pydantic Schemas, CRUD
Tag 3 (11.05.) : REST API Endpunkte, API-Tests, Frontend-Init (Vite)
Tag 4 (12.05.) : React Komponenten, Fetch-API, CSS Styling, .env Config
Tag 5 (13.05.) : Refactoring, README.md, Protokolle, Gitattributes, AWS Deployment
```

**Gesamt: 23 Commits** — Alle mit professionellen, englischen Commit-Nachrichten.

---

## 🎯 NÄCHSTE MÖGLICHE SCHRITTE

### Erweiterungen (Features)
- [ ] Aufgaben nach Erledigt / Offen filtern
- [ ] Aufgaben bearbeiten (Titel/Beschreibung ändern)
- [ ] Prioritäten für Aufgaben (Hoch, Mittel, Niedrig)
- [ ] Drag & Drop zur Sortierung
- [ ] Dark Mode Toggle
- [ ] Login / Authentifizierung (JWT)
- [ ] Unit-Tests für Backend (pytest)
- [ ] Dockerfile für Containerisierung

### AWS Verbesserungen
- [ ] Elastic IP erstellen (feste öffentliche IP)
- [ ] Domain registrieren + Let's Encrypt (echtes SSL)
- [ ] S3 Backup für Datenbank einrichten
- [ ] CloudWatch Monitoring aktivieren
- [ ] Auto-Scaling Group konfigurieren

### IHK-relevante Dokumentation
- [ ] Lastenheft / Pflichtenheft als PDF
- [ ] ER-Diagramm der Datenbank
- [ ] Architektur-Diagramm (3-Schichten)
- [ ] Netzwerk-Diagramm (AWS-Infrastruktur)
- [ ] Testprotokolle / Screenshots
- [ ] Benutzerhandbuch
- [ ] Tagesprotokolle für Tag 1, 3, 4 erstellen

---

## ⚠️ BEKANNTE HINWEISE / GRENZEN

1. **Python 3.14 auf Mac** — FastAPI läuft lokal nicht (pydantic-core Inkompatibilität). Auf dem AWS-Server läuft Python 3.10 → alles funktioniert.
2. **SQLite** speichert die Datenbank `tasks.db` im Projektroot.
3. **CORS** ist auf `http://localhost:5173` eingestellt (lokal). Auf AWS läuft alles über Nginx.
4. **SSL-Zertifikat** ist selbst-signiert → Browser zeigt Warnung an (für Demo normal).
5. **EC2-Instanz ist gestoppt** — muss bei Bedarf neu gestartet werden (IP ändert sich!).

---

## 🛠️ SCHNELL-BEFEHLE

```bash
# Projekt öffnen
cd /Users/danialahmed/aufgabenloescher

# Git-Status prüfen
git status

# Commit-Historie ansehen
git log --oneline --graph

# Änderungen pushen (Token nötig)
git push origin main

# Backend starten (lokal)
cd backend && source venv/bin/activate && uvicorn main:app --reload

# Frontend starten (lokal)
cd frontend && npm run dev

# AWS-Instanz starten
aws ec2 start-instances --instance-ids i-08a82ffebd6802307 --profile Danial --region eu-central-1

# AWS-Instanz stoppen
aws ec2 stop-instances --instance-ids i-08a82ffebd6802307 --profile Danial --region eu-central-1
```

---

## 📞 SUPPORT

Bei Fragen oder Problemen:
1. Diese Datei lesen
2. `README.md` im Projektroot lesen
3. `dokumentation/AWS-DEPLOYMENT.md` für AWS-Fragen
4. GitHub-Issues erstellen oder Dozentin fragen

---

**Stand:** Projekt ist vollständig entwickelt, dokumentiert und auf AWS deployed. Instanz ist aktuell gestoppt. Bereit für Abgabe oder Erweiterung. 🎓
