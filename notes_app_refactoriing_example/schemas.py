from pydantic import BaseModel
from typing import Optional

class Note(BaseModel):
    text: str

class UpdateNote(BaseModel):
    text: Optional[str] = None
