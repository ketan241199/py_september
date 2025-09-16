# api/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --- Database Setup ---
DATABASE_URL = "sqlite:///./movies.db"  # change to PostgreSQL if needed

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String, index=True)
    rating = Column(Integer)


Base.metadata.create_all(bind=engine)


# --- Pydantic Schemas ---
class MovieSchema(BaseModel):
    title: str
    genre: str
    rating: int

    class Config:
        orm_mode = True


# --- FastAPI App ---
app = FastAPI(title="Movie API", version="1.0")


@app.get("/")
def health_check():
    return {"status": "ok", "message": "API is running"}


@app.post("/movies", response_model=MovieSchema)
def create_movie(movie: MovieSchema):
    db = SessionLocal()
    db_movie = Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    db.close()
    return db_movie


@app.get("/movies", response_model=List[MovieSchema])
def get_movies():
    db = SessionLocal()
    movies = db.query(Movie).all()
    db.close()
    return movies


@app.get("/movies/{movie_id}", response_model=MovieSchema)
def get_movie(movie_id: int):
    db = SessionLocal()
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    db.close()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    db = SessionLocal()
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        db.close()
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(movie)
    db.commit()
    db.close()
    return {"status": "deleted", "id": movie_id}
