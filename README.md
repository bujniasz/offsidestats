# OffsideStats API

Simple football stats API built with FastAPI.  

---

## 🔧 Project structure

.
├── app/ # FastAPI app with endpoints and JSON data
├── compose/ # Docker Compose files (dev & prod)
├── Dockerfile # Backend image definition
├── Makefile # CLI shortcuts
├── requirements.txt # Python dependencies


---

## 🚀 Quick start

### Development
```bash
make dev         # start API locally with autoreload
make dev-shell   # open bash inside container

Production

make prod        # run API in detached mode

Docs available at: http://localhost:8000/docs
✅ Features

    FastAPI backend with sample endpoints

    JSON as temporary data source

    Docker + Compose setup (dev & prod)

    Makefile for simplified commands