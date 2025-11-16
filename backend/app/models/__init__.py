from pydantic import BaseModel, Field, conint, confloat

class RawPost(BaseModel):
    post_id: str
    timestamp: str
    username: str
    content: str

class Sentiment(BaseModel):
    positive: float
    negative: float
    neutral: float

class PostSentiment(BaseModel):
    post_id: str
    content: str
    author: str
    likes: int
    views: int
    sentiment: Sentiment

class PostEntity(BaseModel):
    post_id: str
    timestamp: str
    username: str
    content: str
    sentiment: Sentiment
    tickers: list[str]

class PriceChanges(BaseModel):
    ticker: str
    one_day: float
    seven_day: float
    one_day_percent: float
    deven_day_percent: float

class PostProcessed(BaseModel):
    post_id: str
    timestamp: str
    username: str
    content: str
    sentiment: Sentiment
    influence_score: float
    price_changes: list[PriceChanges]
