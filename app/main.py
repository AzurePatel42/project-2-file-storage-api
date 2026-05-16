from fastapi import FastAPI
from app.routers import files, health
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

# Include routers
app.include_router(files.router, prefix="/files", tags=["Files"])
app.include_router(health.router, prefix="/health", tags=["Health"])

@app.get("/")
def root():
    return {"message": "Project 2 File Storage API is running successfully and KTS is watching"}
