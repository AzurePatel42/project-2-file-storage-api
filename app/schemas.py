from datetime import datetime
from pydantic import BaseModel


class FileBase(BaseModel):
    filename: str
    content_type: str
    size: int


class FileCreate(FileBase):
    pass


class File(FileBase):
    id: int
    blob_url: str
    uploaded_at: datetime

    class Config:
        orm_mode = True
