from fastapi import APIRouter, HTTPException, Depends
from models import Post

router = APIRouter(prefix="/admin", tags=["Admin"])

ADMIN_TOKEN = "af398a03b71934775fd0c1e898b59a7b67a0c549e7c6eb38"

def check_admin(token: str):
    if token != ADMIN_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True

@router.get("/pending")
async def get_pending(token: str):
    check_admin(token)
    return await Post.find(Post.approved == False).to_list()

@router.post("/approve/{post_id}")
async def approve_post(post_id: str, token: str):
    check_admin(token)
    post = await Post.get(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post.approved = True
    await post.save()
    return {"message": f"Post '{post.title}' approved"}
