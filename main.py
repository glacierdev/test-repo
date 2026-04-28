"""Small demo module for the Glacier presentation pipeline."""

from __future__ import annotations


def greet(name: str) -> str:
    """Return a friendly greeting for the demo output."""
    clean_name = name.strip() or "friend"
    return f"Hello, {clean_name}!"


def add(left: int, right: int) -> int:
    return left + right


def divide(left: float, right: float) -> float:
    if right == 0:
        raise ValueError("right must not be zero")
    return left / right


if __name__ == "__main__":
    print(greet("Glacier"))
    print(f"2 + 3 = {add(2, 3)}")
