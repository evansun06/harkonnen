
"""

    Sentiment Analyzed Script

"""

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
from app.models import RawPost, Sentiment, PostSentiment

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


def get_sentiments(RawPosts:list[RawPost]) -> list[PostSentiment]: 
    """ Pipeline component: Aquire sentiment score for all raw posts"""

    return list[PostSentiment]


if __name__ == "__main__":
    print(get_sentiment("THe STOCK MARKET IS CRASHING SELL NOW"))