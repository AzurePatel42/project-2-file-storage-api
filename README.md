# **Project 2 — Cloud File Storage API**

<p align="left">

  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-File%20Storage%20API-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Azure-Blob%20Storage-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-Containerized-0db7ed?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" />
  <img src="https://img.shields.io/badge/Deployed%20on-Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" />

</p>

A production‑ready **Cloud File Storage API** built with FastAPI, PostgreSQL, Docker, and Azure Blob Storage.  
Supports uploading, downloading, deleting files, and storing metadata securely.

---

## 📌 **Overview**

This API provides a scalable cloud‑native file storage solution using:

- FastAPI (Python)
- PostgreSQL (SQLAlchemy ORM)
- Azure Blob Storage
- Docker & Docker Compose
- GitHub Actions CI/CD
- Azure App Service (Web App for Containers)

✔ Upload files  
✔ Download files  
✔ Delete files  
✔ Metadata stored in PostgreSQL  
✔ File content stored in Azure Blob Storage  

---

## 🏗️ **Architecture**

```
                ┌──────────────────────────┐
                │      FastAPI Backend     │
                │  (app/main.py, routers)  │
                └─────────────┬────────────┘
                              │
                              │ Metadata (JSON)
                              ▼
                ┌──────────────────────────┐
                │       PostgreSQL DB      │
                │   (file metadata only)   │
                └─────────────┬────────────┘
                              │
                              │ File Content (Binary)
                              ▼
                ┌──────────────────────────┐
                │    Azure Blob Storage    │
                │  (actual file storage)   │
                └──────────────────────────┘
```

---

## 📁 **Project Structure**

```
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

---

## ⚙️ **Environment Variables**

Create a `.env` file:

```
AZURE_STORAGE_CONNECTION_STRING=your_connection_string
AZURE_CONTAINER_NAME=your_container
DATABASE_URL=postgresql://postgres:password@db:5432/files_db
```

---

## ▶️ **Running Locally (Docker Compose)**

```
docker-compose up --build
```

API will be available at:

```
http://localhost:8000
```

Swagger docs:

```
http://localhost:8000/docs
```

---

## 🔌 **API Endpoints**

### **File Operations**

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/files/upload` | Upload a file |
| GET | `/files/{file_id}` | Download a file |
| DELETE | `/files/{file_id}` | Delete a file |

### **Health Check**

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | API health status |

---

## ☁️ **Deploying to Azure (Web App for Containers)**

### 1️⃣ Build Docker image

```
docker build -t file-storage-api .
```

### 2️⃣ Push to Azure Container Registry (ACR)

```
az acr build --registry <ACR_NAME> --image file-storage-api:v1 .
```

### 3️⃣ Deploy to Azure Web App for Containers

```
az webapp create \
  --resource-group <RESOURCE_GROUP> \
  --plan <APP_SERVICE_PLAN> \
  --name <WEBAPP_NAME> \
  --deployment-container-image-name <ACR_NAME>.azurecr.io/file-storage-api:v1
```

### 4️⃣ Configure environment variables

```
az webapp config appsettings set \
  --resource-group <RESOURCE_GROUP> \
  --name <WEBAPP_NAME> \
  --settings \
  AZURE_STORAGE_CONNECTION_STRING="..." \
  AZURE_CONTAINER_NAME="..." \
  DATABASE_URL="..."
```

---

## 🔮 **Future Enhancements**

- JWT authentication  
- File versioning  
- Public/private access controls  
- File preview support  
- Async background processing  

---

## 📝 **About**

Cloud File Storage API using FastAPI, PostgreSQL, Docker, and Azure Blob Storage.
