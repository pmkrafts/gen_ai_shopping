import re
from typing import Tuple

# Simple keyword lists. Expand these as needed for production.
OFF_TOPIC_KEYWORDS = [
    "politics",
    "election",
    "medical",
    "doctor",
    "diagnosis",
    "legal",
    "lawyer",
    "investment",
    "stock market",
    "crypto",
    "bitcoin",
]

PROFANITY_LIST = [
    "badword1",
    "badword2",
]


def is_off_topic(text: str) -> bool:
    """Return True if the input is not related to shopping/clothing."""
    return any(keyword in text.lower() for keyword in OFF_TOPIC_KEYWORDS)


def has_profanity(text: str) -> bool:
    """Return True if the input contains profanity."""
    return any(word in text.lower() for word in PROFANITY_LIST)


def price_sanity_check(price: float | None) -> bool:
    """Return True if the price is within a reasonable range."""
    if price is None:
        return True
    return 0 < price < 1_000_000


def apply_guardrails(text: str) -> Tuple[bool, str]:
    """Check input against guardrails.

    Returns (is_allowed, message). If is_allowed is False, message is the
    response the agent should return instead of processing the input.
    """
    if not text or not text.strip():
        return False, "I didn't catch that. Could you please say something about clothing or shopping?"

    if has_profanity(text):
        return False, "Please keep the conversation respectful. I'm here to help with clothing and shopping."

    if is_off_topic(text):
        return False, "I'm a clothing store assistant, so I can only help with fashion, outfits, products, and shopping. Let me know how I can help with that!"

    return True, ""
