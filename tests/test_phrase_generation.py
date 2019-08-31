"""Validate sentence created by random_phrase.py."""

from click.testing import CliRunner

import phrasegen.cli
from phrasegen.generator import random_phrase


def validate(test_phrase: str) -> None:
    """Validate compliance to set rules for a given test phrase.

    :param test_prhase: Sentence to validate.
    :return: True or false depending if the validation step passed or not.

    """
    vocabulary = random_phrase.get_vocabulary()
    for values in vocabulary.values():
        assert any(word.lower() in test_phrase.lower() for word in values)


def test_phrase_generation() -> None:
    """Test if all necessary features are present in phrase."""
    test_phrase = random_phrase.generate_phrase()
    validate(test_phrase)


def test_cli() -> None:
    """Test if CLI tool works."""
    runner = CliRunner()
    result = runner.invoke(phrasegen.cli.main, ["--theme", "DevOps"])
    assert result.exit_code == 0
    validate(result.output.split("\n")[1])
