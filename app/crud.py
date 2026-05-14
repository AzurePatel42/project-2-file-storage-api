from sqlalchemy.orm import Session
from app import models, schemas


def get_file(db: Session, file_id: int):
    return db.query(models.File).filter(models.File.id == file_id).first()


def get_files(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.File).offset(skip).limit(limit).all()


def create_file(db: Session, file_data: schemas.FileCreate, blob_url: str):
    db_file = models.File(
        filename=file_data.filename,
        content_type=file_data.content_type,
        size=file_data.size,
        blob_url=blob_url
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file


def delete_file(db: Session, file_id: int):
    file_obj = db.query(models.File).filter(models.File.id == file_id).first()
    if file_obj:
        db.delete(file_obj)
        db.commit()
    return file_obj
