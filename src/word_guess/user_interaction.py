"""User input helpers for the CLI."""

import sys
import termios
import tty


def get_single_char() -> str:
    """Read a single character without requiring Enter."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def user_interaction(
    message: str,
    entry_type: str = "string",
    single_entry: int = 0,
) -> str | int:
    """Prompt the user and return typed string or int."""
    if single_entry == 1:
        user_entry = get_single_char()
    else:
        user_entry = input(message)
    if entry_type == "int":
        try:
            return int(user_entry)
        except ValueError:
            return -1
    return user_entry
