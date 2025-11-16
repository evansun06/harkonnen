
"""

    Sentiment Analyzed Script

"""

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
from app.models.models import RawPost, Sentiment, PostSentiment
import numpy as np

# Init Tokenizer + Model
tok = AutoTokenizer.from_pretrained("ProsusAI/finbert")
mod = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

def get_sentiment(content:str) -> Sentiment:
    """Return sentiment object for a single post"""
    inputs = tok(content, return_tensors="pt", truncation=True, padding=True)
    logits = mod(**inputs).logits.detach().numpy()[0]
    probs = softmax(logits)

    sent:Sentiment = Sentiment(
        positive = probs[0],
        negative = probs[1],
        neutral = probs[2]
    )

    return sent


def get_sentiment_batch(posts: list[RawPost]) -> list[PostSentiment]:
    """Batch call a list of raw posts and return a list of PostSentiment objects"""
    # 1. Extract all text contents
    contents = [p.content for p in posts]

    # 2. Tokenize as a single batch
    inputs = tok(
        contents,
        return_tensors="pt",
        truncation=True,
        padding=True
    )

    # 3. Single forward pass through FinBERT
    logits = mod(**inputs).logits.detach().numpy()  # shape: (N, 3)

    # 4. Softmax for each row
    probs = softmax(logits, axis=1)

    # 5. Build output list
    results: list[PostSentiment] = []

    for post, prob in zip(posts, probs):
        sentiment = Sentiment(
            positive=float(prob[0]),
            negative=float(prob[1]),
            neutral=float(prob[2])
        )

        result = PostSentiment(
            **post.model_dump(),
            sentiment=sentiment
        )

        results.append(result)

    return results


if __name__ == "__main__":
    # Simple test RawPosts
    test_posts = [
        RawPost(
            post_id="1",
            timestamp="2025-02-16T10:00:00Z",
            username="elonmusk",
            content="Tesla stock will soar!"
        ),
        RawPost(
            post_id="2",
            timestamp="2025-02-16T10:05:00Z",
            username="billgates",
            content="New tariffs have been implaced on rare earth metals imports"
        ),
    ]

    # Run batch sentiment analysis
    results = get_sentiment_batch(test_posts)

    # Print results nicely
    for r in results:
        print("\nPost ID:", r.post_id)
        print("User:", r.username)
        print("Content:", r.content)
        print("Sentiment:")
        print("  Positive:", r.sentiment.positive)
        print("  Negative:", r.sentiment.negative)
        print("  Neutral:", r.sentiment.neutral)
