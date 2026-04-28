import os

import pytest

from main import add, divide, greet


def test_greet_uses_name() -> None:
    assert greet("Glacier") == "Hello, Glacier!"


def test_greet_falls_back_for_blank_name() -> None:
    assert greet("   ") == "Hello, friend!"


def test_adds_numbers() -> None:
    assert add(2, 3) == 5


def test_divides_numbers() -> None:
    assert divide(10, 2) == 5


def test_divide_rejects_zero() -> None:
    with pytest.raises(ValueError, match="must not be zero"):
        divide(10, 0)


def test_pipeline_env_is_available() -> None:
    assert os.environ.get("DEMO_GREETING") == "Hello from Glacier"
