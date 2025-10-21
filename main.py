from fastapi import FastAPI
from beanie import init_beanie
import motor.motor_asyncio
from routes import posts, admin
from models import Post

app = FastAPI(title="Secure Blog API")

@app.on_event("startup")
async def app_init():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://ckulthe56_db_user:N3RmF60r9xaBtrBU@cluster0.tfyywqo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    await init_beanie(database=client.blog_db, document_models=[Post])

# Root route
@app.get("/")
async def root():
    return {"status": "FastAPI Secure Blog is running 🚀"}

app.include_router(posts.router)
app.include_router(admin.router)


"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"status": "FastAPI blog is running 🚀"}
"""

