# AI Job Matcher

AI-powered job matching application built with FastAPI and Docker.

## Features

- Analyze job descriptions
- Compare candidate skills with job requirements
- Upload PDF CVs
- Extract skills automatically
- Calculate match score
- REST API with FastAPI
- Dockerized application

## Tech Stack

- Python
- FastAPI
- Docker
- Uvicorn
- PyPDF

## Endpoints

### GET /

Health check endpoint.

### POST /match

Compare a job description against a candidate profile.

### POST /match-pdf

Upload a PDF CV and compare it against a job description.

## Run locally

```bash
uvicorn main:app --reload
```

## Run with Docker

```bash
docker build -t ai-job-matcher .
docker run -p 8000:8000 ai-job-matcher
```