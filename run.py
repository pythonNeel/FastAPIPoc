from fastapi import FastAPI
import uvicorn
from app import models
from app.database import engine
from app.routes import org_api, user_api

# For Creating Tables According to Models
models.Base.metadata.create_all(bind=engine)

# Creating App Instance
app = FastAPI()

app.include_router(org_api.router)
app.include_router(user_api.router)


@app.get("/")
def home():
    return "Hello World"


if __name__ == "__main__":
    uvicorn.run("run:app", host="0.0.0.0", port=8000, reload=True)
