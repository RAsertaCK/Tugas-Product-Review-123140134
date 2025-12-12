from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
import json

from . import models, schemas, crud
from .database import engine, get_db
from .services.sentiment_analyzer import SentimentAnalyzer
from .services.keypoint_extractor import KeyPointExtractor

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Review Analyzer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sentiment_analyzer = SentimentAnalyzer()
keypoint_extractor = KeyPointExtractor()

@app.get("/")
def read_root():
    return {"message": "Product Review Analyzer API is running!"}

@app.post("/api/analyze-review", response_model=schemas.ReviewAnalysisResult)
def analyze_review(review_input: schemas.ReviewInput, db: Session = Depends(get_db)):
    """Menganalisis ulasan baru, menyimpan, dan mengembalikan hasilnya."""
    review_text = review_input.review_text.strip()
    
    if not review_text:
        raise HTTPException(status_code=400, detail="Review text cannot be empty")
    
    sentiment = sentiment_analyzer.analyze(review_text)
    
    key_points = keypoint_extractor.extract(review_text)
    
    analysis_result = schemas.ReviewAnalysisResult(
        review_text=review_text,
        sentiment=sentiment,
        key_points=key_points
    )
    
    try:
        db_result = crud.create_review_result(db=db, result=analysis_result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database save failed: {e}")

    return schemas.ReviewAnalysisResult(
        id=db_result.id,
        review_text=db_result.review_text,
        sentiment=db_result.sentiment,
        key_points=json.loads(db_result.key_points) if db_result.key_points else [],
        created_at=db_result.created_at
    )

@app.get("/api/reviews", response_model=list[schemas.ReviewAnalysisResult])
def get_all_reviews(db: Session = Depends(get_db)):
    """Mengambil semua hasil analisis ulasan yang tersimpan."""
    return crud.get_reviews(db=db)