# 🤖 AI Attendance App

An AI-powered attendance management system built with **Python, Streamlit, Face Recognition, and Supabase**.

The application uses face recognition to identify registered users and records attendance in a **Supabase PostgreSQL database**.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Requirements](#-requirements)
- [Project Structure](#-project-structure)
- [Development Setup](#-development-setup)
- [Environment Variables](#-environment-variables)
- [Running the Application](#-running-the-application)
- [Production Deployment](#-production-deployment)
- [Production Configuration](#-production-configuration)
- [Docker Deployment](#-docker-deployment)
- [Nginx Reverse Proxy](#-nginx-reverse-proxy)
- [systemd Service](#-running-as-a-linux-service)
- [Database](#-database)
- [Face Recognition](#-face-recognition)
- [Security](#-security)
- [Troubleshooting](#-troubleshooting)
- [Updating the Application](#-updating-the-application)
- [License](#-license)

---

# 📌 Overview

The **AI Attendance App** provides an attendance management workflow using facial recognition.

A typical workflow is:

```text
                 ┌──────────────────┐
                 │   User Camera    │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Image Processing │
                 │     Pillow       │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Face Detection   │
                 │      dlib        │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Face Recognition │
                 │ face_recognition │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Identify Person  │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │    Supabase      │
                 │   PostgreSQL     │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Attendance Data  │
                 └──────────────────┘
```

---

# ✨ Features

- Face-based attendance recognition
- User registration
- Face recognition
- Attendance recording
- Supabase PostgreSQL database
- Password hashing with bcrypt
- QR code generation
- Image processing
- Streamlit web interface
- Machine-learning utilities through scikit-learn

> Update this section as additional application features are implemented.

---

# 🛠 Technology Stack

| Technology              | Purpose                               |
| ----------------------- | ------------------------------------- |
| Python                  | Application development               |
| Streamlit               | Web application/UI                    |
| NumPy                   | Numerical computation                 |
| Pandas                  | Data processing                       |
| scikit-learn            | Machine learning utilities            |
| dlib                    | Face detection/recognition dependency |
| face_recognition_models | Face recognition models               |
| Pillow                  | Image processing                      |
| Supabase                | PostgreSQL database/backend           |
| bcrypt                  | Password hashing                      |
| Segno                   | QR code generation                    |
| Git                     | Version control                       |

---

# 📦 Requirements

## Python

Recommended:

```text
Python 3.10+
```

Check your Python version:

```bash
python --version
```

or Linux:

```bash
python3 --version
```

---

# 📄 requirements.txt

The project currently uses:

```text
numpy
pandas

# Face Recognition
scikit-learn
dlib-bin
git+https://github.com/ageitgey/face_recognition_models
setuptools<70.0.0

# Database
supabase

# Security
bcrypt

# QR Code
segno

# Image Processing
pillow

# Web Framework
streamlit
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 📁 Project Structure

Recommended structure:

```text
AI_Attendance_APP/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
├── .env
│
├── venv/
│
├── pages/
│   └── ...
│
├── services/
│   └── ...
│
├── models/
│   └── ...
│
├── utils/
│   └── ...
│
├── components/
│   └── ...
│
├── assets/
│   └── ...
│
├── data/
│   └── ...
│
└── tests/
    └── ...
```

The exact structure should reflect the actual project.

---

# 👨‍💻 Development Setup

## 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

Navigate to the project:

```bash
cd AI_Attendance_APP
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell reports that script execution is disabled:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate:

```powershell
.\venv\Scripts\Activate.ps1
```

---

### Windows CMD

```cmd
venv\Scripts\activate
```

---

### Linux / macOS

```bash
source venv/bin/activate
```

After activation, you should see:

```text
(venv)
```

at the beginning of your terminal prompt.

---

# 📥 Install Dependencies

Upgrade pip first:

```bash
python -m pip install --upgrade pip
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

Verify:

```bash
pip list
```

Check for dependency conflicts:

```bash
pip check
```

---

# 🔐 Environment Variables

The application uses Supabase, so database credentials should **not** be hard-coded in the source code.

Create:

```text
.env
```

Example:

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_key
```

If additional application configuration is required:

```env
APP_ENV=development
DEBUG=true

SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_key
```

---

# ⚠️ Never Commit `.env`

Add the following to `.gitignore`:

```gitignore
.env
.env.*
venv/
.venv/
__pycache__/
*.pyc
.streamlit/secrets.toml
```

Use `.env.example` to document required variables without exposing secrets:

```env
APP_ENV=development
DEBUG=true

SUPABASE_URL=
SUPABASE_KEY=
```

---

# ▶️ Running the Application

Make sure the virtual environment is activated.

Run:

```bash
streamlit run app.py
```

The application should be available at:

```text
http://localhost:8501
```

Alternatively:

```bash
python -m streamlit run app.py
```

---

# 🧪 Development Mode

For development:

```bash
streamlit run app.py
```

You can explicitly expose Streamlit on the local network:

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Use `0.0.0.0` carefully because it allows other machines on the network to connect to the application.

---

# 🗄 Database — Supabase

The application uses **Supabase**, which provides a PostgreSQL database and related backend services.

A typical database architecture:

```text
AI Attendance App
       │
       │ Supabase Client
       ▼
┌─────────────────────┐
│      Supabase       │
│                     │
│    PostgreSQL       │
│                     │
│  ┌───────────────┐  │
│  │    users      │  │
│  ├───────────────┤  │
│  │  attendance   │  │
│  ├───────────────┤  │
│  │     ...       │  │
│  └───────────────┘  │
└─────────────────────┘
```

The actual tables should be documented here as the database schema evolves.

For example:

| Table        | Purpose                   |
| ------------ | ------------------------- |
| `users`      | Registered users          |
| `attendance` | Attendance records        |
| `...`        | Application-specific data |

---

# 👤 Face Recognition

The application uses the following components for face recognition:

### dlib

Used as a core computer-vision dependency.

### face_recognition_models

Provides the face-recognition model data used by the face-recognition workflow.

### Pillow

Used for image loading and preprocessing.

### NumPy

Used for numerical operations involving image/face data.

The general pipeline is:

```text
Camera / Image
      │
      ▼
   Pillow
      │
      ▼
Image preprocessing
      │
      ▼
    dlib
      │
      ▼
Face detection / encoding
      │
      ▼
Face comparison
      │
      ▼
Recognized user
      │
      ▼
Attendance record
```

---

# 📱 QR Code Generation

The application uses **Segno** for QR-code generation.

Install it through:

```bash
pip install segno
```

It is already included in:

```text
requirements.txt
```

---

# 🔒 Password Security

The application uses `bcrypt` for password hashing.

Passwords should **never** be stored as plain text.

Correct workflow:

```text
User Password
      │
      ▼
    bcrypt
      │
      ▼
Password Hash
      │
      ▼
Database
```

During login:

```text
Entered Password
      │
      ▼
bcrypt verification
      │
      ▼
Stored Hash
      │
      ▼
Authenticated / Rejected
```

---

# 🏭 Production Deployment

For production, the recommended architecture is:

```text
                     Internet
                        │
                        ▼
                ┌──────────────┐
                │    Nginx     │
                │ HTTPS / SSL  │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │  Streamlit   │
                │    :8501     │
                └──────┬───────┘
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
      Face Recognition       Supabase
       dlib / models        PostgreSQL
```

For production:

- Disable debug mode.
- Do not expose Streamlit directly to the public internet when Nginx can be used.
- Use HTTPS.
- Keep secrets outside source control.
- Use a process manager such as `systemd` or Docker.
- Configure automatic restart.
- Monitor logs.
- Back up important data.

---

# 🐧 Production Setup — Linux

## 1. Install System Dependencies

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git
```

Verify:

```bash
python3 --version
```

---

## 2. Clone Application

```bash
git clone <YOUR_REPOSITORY_URL>
cd AI_Attendance_APP
```

---

## 3. Create Virtual Environment

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Verify:

```bash
pip check
```

---

# ⚠️ Face Recognition Dependency

The face-recognition stack contains native/binary components.

In particular:

```text
dlib-bin
face_recognition_models
```

can be more sensitive to:

- Python version
- Operating system
- CPU architecture
- pip version
- binary compatibility

Therefore, test the complete installation on the target production server before switching production traffic.

A useful installation test is:

```bash
python -c "import dlib; print('dlib OK')"
```

and:

```bash
python -c "from PIL import Image; print('Pillow OK')"
```

Also verify the application's actual face-recognition workflow before deployment.

---

# ⚙️ Production Environment

Create the production environment configuration:

```bash
nano .env
```

Example:

```env
APP_ENV=production
DEBUG=false

SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_production_key
```

Use production credentials only on the production server.

---

# 🚀 Start Streamlit in Production

Run Streamlit locally on the server:

```bash
streamlit run app.py \
  --server.address 127.0.0.1 \
  --server.port 8501 \
  --server.headless true
```

Or:

```bash
python -m streamlit run app.py \
  --server.address 127.0.0.1 \
  --server.port 8501 \
  --server.headless true
```

---

# 🔄 Running as a Linux Service

Create:

```bash
sudo nano /etc/systemd/system/ai-attendance.service
```

Example:

```ini
[Unit]
Description=AI Attendance Streamlit Application
After=network.target

[Service]
Type=simple

User=ubuntu
Group=ubuntu

WorkingDirectory=/opt/AI_Attendance_APP

Environment="PATH=/opt/AI_Attendance_APP/venv/bin"

ExecStart=/opt/AI_Attendance_APP/venv/bin/python -m streamlit run app.py --server.address 127.0.0.1 --server.port 8501 --server.headless true

Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Replace:

```text
/opt/AI_Attendance_APP
```

with your actual project path.

Then:

```bash
sudo systemctl daemon-reload
```

Enable:

```bash
sudo systemctl enable ai-attendance
```

Start:

```bash
sudo systemctl start ai-attendance
```

Check:

```bash
sudo systemctl status ai-attendance
```

Restart:

```bash
sudo systemctl restart ai-attendance
```

Stop:

```bash
sudo systemctl stop ai-attendance
```

---

# 📜 Production Logs

View application logs:

```bash
sudo journalctl -u ai-attendance
```

Follow logs:

```bash
sudo journalctl -u ai-attendance -f
```

View recent logs:

```bash
sudo journalctl -u ai-attendance -n 100
```

---

# 🌐 Nginx Reverse Proxy

Install Nginx:

```bash
sudo apt install -y nginx
```

Create a site configuration:

```bash
sudo nano /etc/nginx/sites-available/ai-attendance
```

Example:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8501;

        proxy_http_version 1.1;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_read_timeout 86400;
    }
}
```

Enable:

```bash
sudo ln -s /etc/nginx/sites-available/ai-attendance \
    /etc/nginx/sites-enabled/ai-attendance
```

Test:

```bash
sudo nginx -t
```

Reload:

```bash
sudo systemctl reload nginx
```

---

# 🔐 HTTPS

Production deployments should use HTTPS.

The architecture should become:

```text
https://your-domain.com
          │
          ▼
        Nginx
          │
          ▼
 Streamlit :8501
```

A TLS certificate can be configured using your preferred certificate provider.

Do not expose sensitive attendance or user information over plain HTTP in production.

---

# 🐳 Docker Deployment

Docker can be used to make the production environment reproducible.

## Dockerfile

Create:

```text
Dockerfile
```

Example:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["python", "-m", "streamlit", "run", "app.py", \
     "--server.address=0.0.0.0", \
     "--server.port=8501", \
     "--server.headless=true"]
```

Build:

```bash
docker build -t ai-attendance-app .
```

Run:

```bash
docker run -d \
    --name ai-attendance-app \
    -p 8501:8501 \
    --restart unless-stopped \
    ai-attendance-app
```

Check:

```bash
docker ps
```

Logs:

```bash
docker logs -f ai-attendance-app
```

---

# 🔐 Docker Environment Variables

Do not put production secrets into the Dockerfile.

Example:

```bash
docker run -d \
    --name ai-attendance-app \
    -p 8501:8501 \
    --restart unless-stopped \
    -e APP_ENV=production \
    -e DEBUG=false \
    -e SUPABASE_URL="https://your-project.supabase.co" \
    -e SUPABASE_KEY="your-key" \
    ai-attendance-app
```

---

# 🧪 Testing Before Production

Before deploying:

### 1. Check Python

```bash
python --version
```

### 2. Check dependencies

```bash
pip check
```

### 3. Test dlib

```bash
python -c "import dlib; print('dlib OK')"
```

### 4. Test Pillow

```bash
python -c "from PIL import Image; print('Pillow OK')"
```

### 5. Test Supabase

Run the application's database connection workflow.

### 6. Run Streamlit

```bash
streamlit run app.py
```

### 7. Test face recognition

Verify:

- Face detection
- Face encoding
- Face matching
- User identification
- Attendance creation

---

# 🔄 Updating Production

Before updating:

```bash
cd /opt/AI_Attendance_APP
```

Pull latest code:

```bash
git pull origin main
```

Activate environment:

```bash
source venv/bin/activate
```

Update dependencies:

```bash
pip install -r requirements.txt
```

Check:

```bash
pip check
```

Restart:

```bash
sudo systemctl restart ai-attendance
```

Verify:

```bash
sudo systemctl status ai-attendance
```

---

# 🛡️ Security Checklist

Before production deployment:

- [ ] `.env` is not committed to Git
- [ ] Supabase credentials are protected
- [ ] Production uses HTTPS
- [ ] Debug mode is disabled
- [ ] Passwords are hashed using bcrypt
- [ ] Database access is restricted appropriately
- [ ] Server firewall is configured
- [ ] Unused ports are closed
- [ ] Attendance data is backed up
- [ ] Application logs are monitored
- [ ] Python dependencies are updated regularly
- [ ] Face-recognition dependencies are tested on the production server

---

# 🧹 Recommended `.gitignore`

```gitignore
# Virtual environments
venv/
.venv/

# Environment variables
.env
.env.*
!.env.example

# Python
__pycache__/
*.py[cod]

# Streamlit secrets
.streamlit/secrets.toml

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Testing
.pytest_cache/
.coverage
htmlcov/

# Logs
*.log

# Local data
data/
```

---

# 🐛 Troubleshooting

## PowerShell activation fails

Run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## Streamlit command not found

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Then:

```bash
pip install -r requirements.txt
```

Alternatively:

```bash
python -m streamlit run app.py
```

---

## Port 8501 already in use

Run on another port:

```bash
streamlit run app.py --server.port 8502
```

---

## Check installed packages

```bash
pip list
```

---

## Check dependency conflicts

```bash
pip check
```

---

## dlib installation/import problem

First verify:

```bash
python -c "import dlib; print(dlib.__version__)"
```

If this fails, verify:

1. Python version
2. Operating system
3. CPU architecture
4. pip version
5. `dlib-bin` installation

Then reinstall dependencies in a fresh virtual environment.

---

# 📊 Development vs Production

| Configuration      | Development      | Production                 |
| ------------------ | ---------------- | -------------------------- |
| Python environment | `venv`           | `venv` / Docker            |
| Streamlit          | Direct           | Behind Nginx               |
| Address            | `localhost`      | `127.0.0.1` internally     |
| HTTPS              | Optional         | Required                   |
| Debug              | Development only | Disabled                   |
| Secrets            | `.env`           | Secure environment/secrets |
| Process manager    | Terminal         | systemd / Docker           |
| Restart            | Manual           | Automatic                  |
| Logs               | Terminal         | journalctl / Docker        |
| Database           | Supabase         | Supabase                   |
| Monitoring         | Optional         | Recommended                |
| Backup             | Recommended      | Required                   |

---

# ⚡ Quick Start

## Windows

```powershell
# Clone
git clone <YOUR_REPOSITORY_URL>

cd AI_Attendance_APP

# Create virtual environment
python -m venv venv

# Activate
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Linux / macOS

```bash
# Clone
git clone <YOUR_REPOSITORY_URL>

cd AI_Attendance_APP

# Create virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# 🏭 Quick Production Start

```bash
git clone <YOUR_REPOSITORY_URL>

cd AI_Attendance_APP

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

python -m streamlit run app.py \
    --server.address 127.0.0.1 \
    --server.port 8501 \
    --server.headless true
```

For production, run Streamlit through `systemd` and place Nginx in front of it.

---

# 📝 Notes

This project depends on native/binary face-recognition components, so the exact Python and operating-system environment should be kept consistent between development and production.

For reproducible deployments, consider pinning dependency versions after validating a working environment.

---

# 📄 License

Add the project license here.

Example:

```text
MIT License
```

---

# 👨‍💻 Development

For bugs, feature requests, or development discussions, create an issue in the project repository.

---

**AI Attendance App**

_Python • Streamlit • Face Recognition • Supabase • PostgreSQL_
