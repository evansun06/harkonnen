"""
    Client endpoints for API service + debugging
"""

from fastapi import APIRouter, Query
from app.models.models import *
from app.api.endpoints import TimeFrame
from app.nlp.rag.query_rag import RagStore


sub_router = APIRouter()

# ----- Sentiment -----

@sub_router.get("/nlp/sentiment/single", response_model=Sentiment)
def get_single_sentiment(content: str):
    pass

@sub_router.post("/nlp/sentiment/batch", response_model=list[Sentiment])
def get_multiple_sentiment(contents: list[str]):
    pass


# ----- Entities -----

@sub_router.get("/nlp/entity/single{content}", response_model={})
def get_entities_for_single_post(content: str, k: int ):
    rag = RagStore()
    return rag.search(str, k)

@sub_router.post("/nlp/entity/batch", response_model=list[list[str]])
def get_entities_for_multiple_posts(contents: list[str]):
    pass

