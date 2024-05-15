from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
from app.routers import routes
from app.logging_config.logging_config import logger

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    try:
        response = await call_next(request)
        logger.info(f"Incoming request: {request.method} {request.url} - Response code: {response.status_code}")
        return response
    except HTTPException as exc:
        logger.error(f"Incoming request: {request.method} {request.url} - Exception: {exc}")
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


@app.get("/")
async def read_root():
    return {"message": "Welcome to the fastapi project of User Management."}


app.include_router(
    routes.router,
    prefix="/user",
    tags=["User Management Service"]
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
