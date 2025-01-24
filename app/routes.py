from fastapi import APIRouter
from pydantic import BaseModel
from .services import EmbeddingService
from .config import settings

router = APIRouter()
service = EmbeddingService(settings.model_path)

class TextRequest(BaseModel):
    text: str

@router.post("/embed")
async def get_embedding(request: TextRequest):
    embedding = service.get_embeddings(request.text)
    return {"embedding": embedding}
