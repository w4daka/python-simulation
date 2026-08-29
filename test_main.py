from main import sum_to


def test_sum_to_zero() -> None:
    assert sum_to(0) == 0


def test_sum_to_one() -> None:
    assert sum_to(1) == 1


def test_sum_to_three() -> None:
    assert sum_to(3) == 6
