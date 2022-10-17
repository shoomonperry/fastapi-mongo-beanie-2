from fastapi import FastAPI
from app.server.database import init_db
from app.server.routes.property import router as Router

app = FastAPI()
app.include_router(Router, tags=["Properties"], prefix="/properties")

@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome to your beanie powered app!"}
