"""
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
"""

from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse
from models import Post
from utils.sanitizer import sanitize_content

router = APIRouter(prefix="/posts", tags=["Posts"])

import re

def sanitize_content(content: str) -> str:
    # remove emails
    content = re.sub(r"\b[\w.-]+@[\w.-]+\.\w{2,4}\b", "[removed]", content)
    
    # remove phone numbers (simple pattern)
    content = re.sub(r"\b\d{10,15}\b", "[removed]", content)
    
    # remove URLs
    content = re.sub(r"https?://\S+|www\.\S+", "[removed]", content)
    
    return content



@router.post("/submit")
async def submit_post(
    title: str = Form(...), 
    content: str = Form(...), 
    author: str = Form("Anonymous")
):
    clean_content = sanitize_content(content)
    post = Post(title=title, content=clean_content, author=author)
    await post.insert()
    return RedirectResponse("/", status_code=303)  # redirect back to landing page

