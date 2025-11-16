"""
    RAG Wrapper for Pipeline integration
"""

from pathlib import Path
from app.nlp.rag.query_rag import RagStore
from app.models.models import PostEntity

def append_rag_results(entity_posts:list[PostEntity], k:int) -> list[PostEntity]:
    """Append tickers to Fuzzy Search"""
    rag = RagStore(Path(__file__).resolve().parent)

    for post in entity_posts:
        results = rag.search(post.content, k)
        # each result is: {"ticker": "...", "score": float, "description": "..."}
        for r in results:
            if(r["ticker"] not in post.tickers):
                post.tickers.append(r["ticker"])

    return entity_posts
