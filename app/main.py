from fastapi import FastAPI
from app.database import Base, engine
from app.routers import match
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Job Matcher",
    version="2.0.0",
    description="AI-powered job matching API built with FastAPI, PostgreSQL and Docker."
)


@app.get("/")
def home():
    return {"message": "AI Job Matcher API is running", "version": "2.0.0"}


app.include_router(match.router)
