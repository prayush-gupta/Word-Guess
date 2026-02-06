"""Application configuration from environment."""

import os


def get_database_url() -> str | None:
    """Return DATABASE_URL, normalizing postgres:// to postgresql://."""
    url = os.environ.get("DATABASE_URL")
    if url and url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)
    return url
