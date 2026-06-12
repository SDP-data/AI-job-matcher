from sqlalchemy.orm import Session
from app import models


def create_match_result(
    db: Session,
    job_title: str,
    job_description: str,
    candidate_profile: str | None,
    cv_filename: str | None,
    match_score: float,
    recommendation: str,
    matching_skills: list[str],
    missing_skills: list[str],
):
    db_match = models.MatchResult(
        job_title=job_title,
        job_description=job_description,
        candidate_profile=candidate_profile,
        cv_filename=cv_filename,
        match_score=match_score,
        recommendation=recommendation,
        matching_skills=", ".join(matching_skills),
        missing_skills=", ".join(missing_skills),
    )

    db.add(db_match)
    db.commit()
    db.refresh(db_match)

    return db_match


def get_match_results(db: Session, limit: int = 10):
    return (
        db.query(models.MatchResult)
        .order_by(models.MatchResult.created_at.desc())
        .limit(limit)
        .all()
    )
