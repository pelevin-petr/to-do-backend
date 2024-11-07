from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from app.db.connection import init_models, drop_models
from app.routers.auth import auth_router
from app.routers.tasks import task_router

app = FastAPI(
    title="ToDo API",
    description="A simple ToDo API",
)
app.include_router(auth_router)
app.include_router(task_router)


@app.exception_handler(Exception)
async def unexpected_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "message": "An unexpected error occurred. Please try again later.",
            "detail": str(exc)
        }
    )


@app.on_event("startup")
async def on_startup():
    try:
        await drop_models()
        await init_models()
    except Exception as e:
        print(f"Ошибка при инициализации: {e}")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
