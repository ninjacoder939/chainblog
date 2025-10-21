from fastapi import FastAPI
from beanie import init_beanie
import motor.motor_asyncio
from routes import posts, admin
from models import Post

app = FastAPI(title="Secure Blog API")

@app.on_event("startup")
async def app_init():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=client.blog_db, document_models=[Post])

app.include_router(posts.router)
app.include_router(admin.router)
