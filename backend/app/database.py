from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic_settings import BaseSettings
import os

# Konfigurasi Pydantic untuk mengambil variabel lingkungan
class Settings(BaseSettings):
    # Mengambil dari .env jika tidak ada, menggunakan default jika DB belum siap
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+psycopg2://user:password@db:5432/review_db")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "dummy_key")

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()

# Setup Engine dan SessionLocal
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency untuk mendapatkan DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()