from fastapi import APIRouter, UploadFile, File, HTTPException
from app.azure_blob import (
    get_blob_client,
    upload_file_to_blob,
    delete_file_from_blob,
    list_files_in_blob
)
from app import schemas

router = APIRouter(prefix="/files", tags=["Files"])


@router.post("/", response_model=schemas.File)
async def upload_file(uploaded_file: UploadFile = File(...)):
    container_client = get_blob_client()

    blob_url = upload_file_to_blob(
        container_client,
        await uploaded_file.read(),
        uploaded_file.filename
    )

    return schemas.File(
        id=0,  # no DB, so dummy ID
        filename=uploaded_file.filename,
        content_type=uploaded_file.content_type,
        size=uploaded_file.size or 0,
        url=blob_url
    )


@router.get("/", response_model=list[schemas.File])
def list_files():
    container_client = get_blob_client()
    files = list_files_in_blob(container_client)
    return files


@router.delete("/{filename}")
def delete_file(filename: str):
    container_client = get_blob_client()
    delete_file_from_blob(container_client, filename)
    return {"message": "File deleted successfully"}
