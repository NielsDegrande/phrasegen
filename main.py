"""Entrypoint for DevOps Onboarding, Case Study 2."""

import click

from phrasegen import random_phrase


@click.command()
@click.option(
    "--theme",
    default="devops",
    help="Specify theme for random sentence generation.",
)
def main(theme: str) -> None:
    """Generate random phrases."""
    print(f"Theme: {theme}.")
    print(random_phrase.generate_phrase())


if __name__ == "__main__":
    main(None)
