# -*- coding: utf-8 -*-
"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """template_name."""
    return None


def example_doctest() -> None:
    """Example.

    Example for how to write a doctest:

    >>> assert example_doctest() is None
    """
    return None


if __name__ == "__main__":
    # pylint: disable=unexpected-keyword-arg
    main(prog_name="template_name")  # pragma: no cover
