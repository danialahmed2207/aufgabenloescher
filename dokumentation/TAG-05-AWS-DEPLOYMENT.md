# Tagesprotokoll — AWS Deployment (Projekttag 5 Erweiterung)

**Datum:** 13. Mai 2026  
**Projekt:** Aufgabenlöscher — Fullstack-Aufgabenverwaltung  
**Entwickler:** Danial Ahmed  
**Dozentin:** annahoff-syntax

---

## 1. Ziele des Deployments

| Nr. | Ziel | Status |
|-----|------|--------|
| 5.1 | Projekt auf AWS EC2 deployen | ✅ Erledigt |
| 5.2 | SSL/HTTPS einrichten | ✅ Erledigt |
| 5.3 | Automatisches Deployment-Skript erstellen | ✅ Erledigt |
| 5.4 | Monitoring / Status-Seite einrichten | ✅ Erledigt |

---

## 2. AWS-Infrastruktur

### 2.1 Erstellte Ressourcen

| Ressource | ID | Details |
|-----------|-----|---------|
| **VPC** | `vpc-08771a5f5401d5547` | Standard-VPC in eu-central-1 |
| **EC2 Instance** | `i-08a82ffebd6802307` | t2.micro, Ubuntu 22.04 LTS |
| **Security Group** | `sg-05c21ee1d31d3f105` | Ports 22, 80, 443, 8000 |
| **SSH Key Pair** | `aufgabenloescher-key` | Für SSH-Zugang |
| **Öffentliche IP** | `3.69.31.130` | Elastic IP (noch nicht zugewiesen) |
| **AWS Account** | `579320645741` | Techstarter Sandbox |

### 2.2 Server-Konfiguration

| Komponente | Software | Port | Zweck |
|------------|----------|------|-------|
| Webserver | Nginx 1.18.0 | 80, 443 | Auslieferung Frontend + SSL |
| Backend | FastAPI + Uvicorn | 8000 | REST API (intern) |
| Datenbank | SQLite | — | Persistente Datenspeicherung |
| Monitoring | Cron + Shell | — | Status-Seite alle 5 Minuten |

---

## 3. Deployment-Schritte

### 3.1 EC2-Instanz erstellen

- **AMI:** Ubuntu 22.04 LTS (`ami-0f7804991cb8f07c4`)
- **Instance Type:** t2.micro (Free Tier)
- **Region:** eu-central-1 (Frankfurt)
- **Key Pair:** `aufgabenloescher-key` (PEM-Datei lokal gesichert)

### 3.2 Security Group konfigurieren

Eingehende Regeln:

| Port | Protokoll | Quelle | Zweck |
|------|-----------|--------|-------|
| 22 | TCP | 0.0.0.0/0 | SSH-Zugang |
| 80 | TCP | 0.0.0.0/0 | HTTP (Frontend) |
| 443 | TCP | 0.0.0.0/0 | HTTPS (SSL) |
| 8000 | TCP | 0.0.0.0/0 | API-Direktzugriff (für Entwicklung) |

### 3.3 Software-Installation auf dem Server

```bash
# System-Pakete
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv nodejs npm git nginx curl

# Node.js 20 LTS (fuer Vite-Kompatibilitaet)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### 3.4 Projekt-Deployment

```bash
# Repository klonen
git clone https://github.com/danialahmed2207/TaskFlow-Fullstack-Aufgabenmanager.git

# Backend einrichten
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend bauen
cd frontend
npm install
npm run build
sudo cp -r dist/* /var/www/aufgabenloescher/
```

### 3.5 Nginx als Reverse Proxy

Konfiguration (`/etc/nginx/sites-available/aufgabenloescher`):
- Port 80 → Weiterleitung auf HTTPS
- Port 443 → SSL + Frontend-Dateien
- `/api/` → Proxy zum Backend (Port 8000)

### 3.6 SSL-Zertifikat (selbst-signiert)

```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/nginx/ssl/aufgabenloescher.key \
  -out /etc/nginx/ssl/aufgabenloescher.crt
```

> **Hinweis:** Für Produktion benötigt man eine Domain + Let's Encrypt. Das selbst-signierte Zertifikat dient der Demo.

### 3.7 Backend als Systemd-Service

Service-Datei: `/etc/systemd/system/aufgabenloescher.service`
- Automatischer Start beim Booten
- Automatischer Neustart bei Absturz
- Logging via `journalctl`

---

## 4. Automatisches Deployment

### 4.1 Deploy-Skript

Pfad: `/usr/local/bin/deploy-aufgabenloescher`

Funktionen:
1. `git pull origin main`
2. Frontend bauen (`npm install && npm run build`)
3. Backend-Abhängigkeiten aktualisieren
4. Nginx + Backend-Services neustarten

### 4.2 Ausführung

```bash
ssh -i aufgabenloescher-key.pem ubuntu@3.69.31.130 'deploy-aufgabenloescher'
```

---

## 5. Monitoring

### 5.1 Status-Seite

- **URL:** `https://3.69.31.130/status.html`
- **Aktualisierung:** Alle 5 Minuten via Cronjob
- **Inhalt:**
  - Service-Status (Backend, Nginx)
  - CPU-Auslastung
  - RAM-Auslastung
  - Festplattennutzung
  - Uptime
  - Direktlinks zur Anwendung

### 5.2 Cronjob

```cron
*/5 * * * * root /usr/local/bin/update-monitor
```

---

## 6. Probleme & Lösungen

| Problem | Ursache | Lösung |
|---------|---------|--------|
| Node.js zu alt (v12) | Ubuntu 22.04 Standard | NodeSource Repository für Node.js 20 |
| Pydantic-Core Kompilierung | Python 3.14 auf Mac | Auf Server läuft Python 3.10 → fertige Wheels |
| Nginx 500 Error | Backslashes in Config | Entfernung von `\$uri` → `$uri` |
| Nginx Permission Denied | Home-Verzeichnis-Zugriff | Frontend nach `/var/www/` kopieren |
| SSL Zertifikat | Keine Domain vorhanden | Selbst-signiertes Zertifikat für Demo |

---

## 7. URLs im Überblick

| Service | URL | Protokoll |
|---------|-----|-----------|
| Anwendung | http://3.69.31.130/ | HTTP |
| Anwendung (sicher) | https://3.69.31.130/ | HTTPS |
| API | https://3.69.31.130/api/ | HTTPS |
| Status-Seite | https://3.69.31.130/status.html | HTTPS |
| Swagger Docs | https://3.69.31.130/api/docs | HTTPS |

---

## 8. SSH-Zugang

```bash
ssh -i /tmp/aufgabenloescher-key.pem ubuntu@3.69.31.130
```

Wichtige Befehle auf dem Server:
```bash
# Services steuern
sudo systemctl {status|restart} aufgabenloescher
sudo systemctl {status|restart} nginx

# Logs ansehen
sudo journalctl -u aufgabenloescher -f
sudo tail -f /var/log/nginx/error.log

# Deploy durchfuehren
deploy-aufgabenloescher
```

---

## 9. Zeitaufwand

| Phase | Zeit |
|-------|------|
| EC2-Instanz erstellen & konfigurieren | 1 Std. |
| Software-Installation (Python, Node, Nginx) | 1 Std. |
| Projekt-Deployment (Frontend + Backend) | 1 Std. |
| Nginx & SSL konfigurieren | 1 Std. |
| Auto-Deploy & Monitoring einrichten | 0,5 Std. |
| Fehlerbehebung (Node, Nginx, Berechtigungen) | 1,5 Std. |
| **Gesamt** | **6 Std.** |

---

## 10. Nächste Schritte / Empfehlungen

- [ ] **Elastic IP** zuweisen (feste öffentliche IP, die nicht wechselt)
- [ ] **Domain registrieren** + Let's Encrypt für echtes SSL
- [ ] **Datenbank-Backup** einrichten (z. B. täglicher Snapshot der SQLite-Datei)
- [ ] **CloudWatch** für erweitertes Monitoring konfigurieren
- [ ] **Auto-Scaling** (für Produktionsumgebungen)

---

*Protokoll erstellt am: 13. Mai 2026*  
*Deployment erfolgreich abgeschlossen!* 🚀
