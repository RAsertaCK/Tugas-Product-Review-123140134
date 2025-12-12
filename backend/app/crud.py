from sqlalchemy.orm import Session
from . import models, schemas
import json 
from typing import List

def create_review_result(db: Session, result: schemas.ReviewAnalysisResult):
    key_points_json = json.dumps(result.key_points)
    
    db_result = models.ReviewResult(
        review_text=result.review_text,
        sentiment=result.sentiment,
        key_points=key_points_json,
    )
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

def get_reviews(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.ReviewAnalysisResult]:
    reviews = db.query(models.ReviewResult).order_by(models.ReviewResult.created_at.desc()).offset(skip).limit(limit).all()
    
    results = []
    for r in reviews:
        key_points_list = json.loads(r.key_points) if r.key_points else []
        
        results.append(schemas.ReviewAnalysisResult(
            id=r.id,
            review_text=r.review_text,
            sentiment=r.sentiment,
            key_points=key_points_list,
            created_at=r.created_at
        ))
    return results