import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.app_routes.upload_utils import upload_router
from src.api.app_routes.chat_utils import chat_routes

app = FastAPI()
origin_list = [
    'http://localhost:3000', 'http://localhost'
]
app.add_middleware(middleware_class=CORSMiddleware, allow_origins=origin_list)
app.include_router(upload_router, prefix="/api/upload")
app.include_router(chat_routes, prefix="/api")


@app.get("/health")
async def health():
    return {"health": "OK"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
