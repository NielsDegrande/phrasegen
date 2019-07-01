"""Actual logic for DevOps Onboarding, Case Study 2."""

from random import choice, choices
from typing import Dict, List


def get_vocabulary() -> Dict[str, List[str]]:
    """Obtain vocabulary dictionary.

    :return: Dictionary with as key a grammatical
             feature and value a list of examples.

    """
    vocabulary = {
        "buzz": [
            "continuous testing",
            "continuous integration",
            "continuous deployment",
            "continuous improvement",
            "devops",
        ],
        "adjectives": [
            "complete",
            "modern",
            "self-service",
            "integrated",
            "end-to-end",
        ],
        "adverbs": [
            "remarkably",
            "enormously",
            "substantially",
            "significantly",
            "seriously",
        ],
        "verbs": [
            "accelerates",
            "improves",
            "enhances",
            "revamps",
            "boosts",
        ],
    }

    return vocabulary


def generate_phrase() -> int:
    """Generate a random phrase given arrays of words.

    :return: A random phrase.

    """
    vocabulary = get_vocabulary()

    adjective = choice(vocabulary["adjectives"])
    subject, object_ = choices(vocabulary["buzz"], k=2)
    verb = choice(vocabulary["verbs"])
    adverb = choice(vocabulary["adverbs"])

    return f"{adjective.capitalize()} {subject} {verb} {object_} {adverb}. "


if __name__ == "__main__":
    print(generate_phrase())
