# AI Job Matcher v2

AI-powered job matching API that compares candidate profiles or PDF CVs against job descriptions, extracts relevant skills, calculates a match score, and stores results in PostgreSQL.

## Features

* Match candidate profiles against job descriptions
* Upload and analyze PDF CVs
* Extract skills automatically
* Calculate match score and recommendation
* Store results in PostgreSQL
* Query historical match results
* Interactive Swagger documentation
* Dockerized deployment

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Docker
* Docker Compose
* PyPDF

## Architecture

```text
Client
   ↓
FastAPI
   ↓
SQLAlchemy
   ↓
PostgreSQL
```

## API Endpoints

| Method | Endpoint   | Description             |
| ------ | ---------- | ----------------------- |
| GET    | /          | Health check            |
| POST   | /match     | Match candidate profile |
| POST   | /match-pdf | Match PDF CV            |
| GET    | /matches   | List stored results     |

## Run Locally

```bash
docker compose up --build
```

Open:

```text
http://localhost:8000/docs
```

## Example Response

```json
{
  "id": 1,
  "job_title": "ML Engineer",
  "match_score": 83.33,
  "recommendation": "Strong match"
}
```

## Learning Goals

This project was built to practice:

* Backend development with FastAPI
* PostgreSQL integration
* SQLAlchemy ORM
* Docker and Docker Compose
* REST API design
* Data persistence

## Author

Sebastián Díaz

Electrical Engineer | Data Scientist | MSc in Data Science & Machine Learning (c)