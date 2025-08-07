from sqlalchemy.orm import Session
from app import models, schemas

def create_translation(db: Session, data: schemas.TranslationCreate):
    translation = models.Translation(
        original_text=data.original_text,
        translated_text=data.translated_text,
        status="new"
    )
    db.add(translation)
    db.commit()
    db.refresh(translation)
    return translation
