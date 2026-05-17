from pydantic import BaseModel


class File(BaseModel):
    id: int
    filename: str
    content_type: str
    size: int
    url: str


class FileCreate(BaseModel):
    filename: str
    content_type: str
    size: int
