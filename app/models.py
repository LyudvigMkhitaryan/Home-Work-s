from sqlalchemy import Column, Integer, String
from app.database import Base

class Translation(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(String, nullable=False)
    translated_text = Column(String, nullable=False)
    status = Column(String, default="new")
