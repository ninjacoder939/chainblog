from fastapi import APIRouter, HTTPException
from models import Post
from utils.sanitizer import sanitize_content

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/submit")
async def submit_post(title: str, content: str, author: str = "Anonymous"):
    clean_content = sanitize_content(content)
    post = Post(title=title, content=clean_content, author=author)
    await post.insert()
    return {"message": "Post submitted for review!"}
