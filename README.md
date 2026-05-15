# Project 2 — Cloud File Storage API

FastAPI • PostgreSQL • Docker • Azure Blob Storage

---

## 📌 Overview

This project is a production-ready Cloud File Storage API built using:

- FastAPI (Python)
- PostgreSQL (SQLAlchemy ORM)
- Azure Blob Storage
- Docker & Docker Compose

It supports:

- Uploading files
- Downloading files
- Deleting files
- Storing metadata in PostgreSQL
- Storing file content in Azure Blob Storage

---

## 🏗️ Architecture

### Components

- FastAPI — REST API backend  
- PostgreSQL — Stores file metadata  
- Azure Blob Storage — Stores file content  
- Docker Compose — Local development environment  
- GitHub Actions — CI/CD pipeline  
- Azure App Service — Deployment target  

---

## 📁 Project Structure

```text
project-2-file-storage-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── azure_blob.py
│   └── routers/
│       ├── files.py
│       └── health.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```