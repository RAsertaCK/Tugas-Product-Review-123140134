# backend/app/schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# Skema Input Review
class ReviewInput(BaseModel):
    review_text: str

# Skema Hasil Analisis (untuk POST Response & GET Response)
class ReviewAnalysisResult(BaseModel):
    id: Optional[int] = None
    review_text: str
    sentiment: str
    key_points: List[str]
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True