from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas
from app.azure_blob import get_blob_client, upload_file_to_blob, delete_file_from_blob


router = APIRouter(prefix="/files", tags=["Files"])


@router.post("/", response_model=schemas.File)
async def upload_file(
    uploaded_file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    container_client = get_blob_client()

    blob_url = upload_file_to_blob(
        container_client,
        await uploaded_file.read(),
        uploaded_file.filename
    )

    file_data = schemas.FileCreate(
        filename=uploaded_file.filename,
        content_type=uploaded_file.content_type,
        size=uploaded_file.size or 0
    )

    db_file = crud.create_file(db, file_data, blob_url)
    return db_file


@router.get("/", response_model=list[schemas.File])
def list_files(db: Session = Depends(get_db)):
    return crud.get_files(db)


@router.get("/{file_id}", response_model=schemas.File)
def get_file(file_id: int, db: Session = Depends(get_db)):
    file_obj = crud.get_file(db, file_id)
    if not file_obj:
        raise HTTPException(status_code=404, detail="File not found")
    return file_obj


@router.delete("/{file_id}")
def delete_file(file_id: int, db: Session = Depends(get_db)):
    file_obj = crud.get_file(db, file_id)
    if not file_obj:
        raise HTTPException(status_code=404, detail="File not found")

    container_client = get_blob_client()
    delete_file_from_blob(container_client, file_obj.filename)

    crud.delete_file(db, file_id)

    return {"message": "File deleted successfully"}
