from pydantic import BaseModel

class TranslationCreate(BaseModel):
    original_text: str
    translated_text: str
