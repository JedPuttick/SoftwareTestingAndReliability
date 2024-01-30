import pytest
from car import Car


def test_min_max_speed_exception():
    with pytest.raises(Exception) as ex:
        car1 = Car("Honda", "Jazz", "HK11ABC", 5, 4, 1.2, 0, 0, 50)
    assert str(ex.value) == "Max speed cannot be less than 1"


def test_min_doors_exception():
    with pytest.raises(Exception) as ex:
        car1 = Car("Honda", "Jazz", "HK11ABC", 0, 4, 1.2, 0, 60, 50)
    assert str(ex.value) == "There cannot be fewer than 1 door"


def test_min_wheels_exception():
    with pytest.raises(Exception) as ex:
        car1 = Car("Honda", "Jazz", "HK11ABC", 2, 2, 1.2, 0, 60, 50)
    assert str(ex.value) == "There cannot be fewer than 3 wheels"
