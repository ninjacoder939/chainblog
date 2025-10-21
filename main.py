from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from beanie import init_beanie
import motor.motor_asyncio
from routes import posts, admin
from models import Post

app = FastAPI(title="Secure Blog API")

templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
async def app_init():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb+srv://ckulthe56_db_user:N3RmF60r9xaBtrBU@cluster0.tfyywqo.mongodb.net/blog_db?retryWrites=true&w=majority&tls=true"
    )
    await init_beanie(database=client.blog_db, document_models=[Post])

# Landing page
@app.get("/")
async def root(request: Request):
    posts_list = await Post.find_all().to_list()
    return templates.TemplateResponse("index.html", {"request": request, "posts": posts_list})

# Include routers
app.include_router(posts.router)
app.include_router(admin.router)

