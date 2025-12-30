from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    title: str
    author: str
    text: str

class UpdatePost(BaseModel):
    title: Optional[str]=None
    author: Optional[str]=None
    text: Optional[str]=None