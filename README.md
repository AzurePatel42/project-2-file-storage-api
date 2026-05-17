# Project 2 — Cloud File Storage API
<p align="left">

  <!-- Python -->
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" />

  <!-- FastAPI -->
  <img src="https://img.shields.io/badge/FastAPI-File%20Storage%20API-009688?style=for-the-badge&logo=fastapi&logoColor=white" />

  <!-- PostgreSQL -->
  <img src="https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql&logoColor=white" />

  <!-- Azure Blob Storage -->
  <img src="https://img.shields.io/badge/Azure-Blob%20Storage-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" />

  <!-- Docker -->
  <img src="https://img.shields.io/badge/Docker-Containerized-0db7ed?style=for-the-badge&logo=docker&logoColor=white" />

  <!-- GitHub Actions -->
  <img src="https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" />

</p>
<img src="https://img.shields.io/badge/Deployed%20on-Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" />



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
