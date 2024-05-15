from fastapi import FastAPI, HTTPException, status
import uvicorn
import routes

app = FastAPI()


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
