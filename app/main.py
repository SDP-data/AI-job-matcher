from fastapi import FastAPI
from app.routers import match

app = FastAPI(
    title="AI Job Matcher",
    version="2.0.0",
    description="AI-powered job matching API built with FastAPI."
)


@app.get("/")
def home():
    return {"message": "AI Job Matcher API is running", "version": "2.0.0"}


app.include_router(match.router)
