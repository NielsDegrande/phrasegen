"""Validate sentence created by random_phrase.py."""

from phrasegen import random_phrase


def test_phrase_generation() -> None:
    """Test if all necessary features are present in phrase."""
    vocabulary = random_phrase.get_vocabulary()
    test_phrase = random_phrase.generate_phrase()

    for values in vocabulary.values():
        assert any(word.lower() in test_phrase.lower() for word in values)
