from main import classify_number


def test_positive() -> None:
    assert classify_number(10) == "positive"


def test_negative() -> None:
    assert classify_number(-3) == "negative"


def test_zero() -> None:
    assert classify_number(0) == "zero"
