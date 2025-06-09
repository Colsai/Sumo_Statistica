"""CLI entry point for :mod:`sumo_statistica`."""

from . import chat


def main() -> None:
    """Delegate to :func:`sumo_statistica.chat.main`."""
    chat.main()


if __name__ == "__main__":
    main()
