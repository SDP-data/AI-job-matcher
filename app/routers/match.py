from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from pypdf import PdfReader
import io

from app.schemas import MatchRequest
from app.database import get_db
from app import crud

router = APIRouter()


SKILLS = [
    "python", "sql", "power bi", "machine learning",
    "data science", "nlp", "docker", "fastapi",
    "aws", "git", "pandas", "numpy", "scikit-learn",
    "tensorflow", "pytorch", "apis", "automation",
    "excel", "power query", "langchain", "rag"
]


def extract_text_from_pdf(file_bytes: bytes) -> str:
    pdf_file = io.BytesIO(file_bytes)
    reader = PdfReader(pdf_file)

    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def find_skills(text: str) -> list[str]:
    text = text.lower()
    return [skill for skill in SKILLS if skill in text]


def calculate_match(job_skills: list[str], candidate_skills: list[str]) -> dict:
    matching_skills = [skill for skill in job_skills if skill in candidate_skills]
    missing_skills = [skill for skill in job_skills if skill not in candidate_skills]

    match_score = round(
        len(matching_skills) / len(job_skills) * 100,
        2
    ) if job_skills else 0

    if match_score >= 75:
        recommendation = "Strong match"
    elif match_score >= 50:
        recommendation = "Moderate match"
    else:
        recommendation = "Low match"

    return {
        "match_score": match_score,
        "recommendation": recommendation,
        "matching_skills": matching_skills,
        "missing_skills": missing_skills
    }


@router.post("/match")
def match_candidate(data: MatchRequest, db: Session = Depends(get_db)):
    job_skills = find_skills(data.job_description)
    candidate_skills = find_skills(data.candidate_profile)

    result = calculate_match(job_skills, candidate_skills)

    saved_result = crud.create_match_result(
        db=db,
        job_title=data.job_title,
        job_description=data.job_description,
        candidate_profile=data.candidate_profile,
        cv_filename=None,
        match_score=result["match_score"],
        recommendation=result["recommendation"],
        matching_skills=result["matching_skills"],
        missing_skills=result["missing_skills"],
    )

    return {
        "id": saved_result.id,
        "job_title": data.job_title,
        "job_skills": job_skills,
        "candidate_skills": candidate_skills,
        **result
    }


@router.post("/match-pdf")
async def match_candidate_pdf(
    job_title: str = Form(...),
    job_description: str = Form(...),
    cv_file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    file_bytes = await cv_file.read()
    cv_text = extract_text_from_pdf(file_bytes)

    job_skills = find_skills(job_description)
    candidate_skills = find_skills(cv_text)

    result = calculate_match(job_skills, candidate_skills)

    saved_result = crud.create_match_result(
        db=db,
        job_title=job_title,
        job_description=job_description,
        candidate_profile=cv_text,
        cv_filename=cv_file.filename,
        match_score=result["match_score"],
        recommendation=result["recommendation"],
        matching_skills=result["matching_skills"],
        missing_skills=result["missing_skills"],
    )

    return {
        "id": saved_result.id,
        "job_title": job_title,
        "cv_filename": cv_file.filename,
        "job_skills": job_skills,
        "candidate_skills": candidate_skills,
        **result
    }
