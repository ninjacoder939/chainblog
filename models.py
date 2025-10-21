from beanie import Document
from pydantic import BaseModel, Field
from datetime import datetime

class Post(Document):
    title: str
    content: str
    author: str = "Anonymous"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    approved: bool = False  # Only admin can set True

    class Settings:
        name = "posts"
