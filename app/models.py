from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from app.database import Base


class MatchResult(Base):
    __tablename__ = "match_results"

    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String(255), nullable=False)
    job_description = Column(Text, nullable=False)
    candidate_profile = Column(Text, nullable=True)
    cv_filename = Column(String(255), nullable=True)
    match_score = Column(Float, nullable=False)
    recommendation = Column(String(100), nullable=False)
    matching_skills = Column(Text, nullable=True)
    missing_skills = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
