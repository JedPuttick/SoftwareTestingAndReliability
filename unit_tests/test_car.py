import pytest
from car import Car


def test_create_car():
    car1 = Car("Honda", "Jazz", "HK11ABC", 5, 4, 1.2, 0, 100, 100)
    assert car1.make == "Honda"
    assert car1.model == "Jazz"
    assert car1.num_plate == "HK11ABC"
    assert car1.doors == 5
    assert car1.wheels == 4
    assert car1.engine_size == 1.2
    assert car1.current_speed == 0
    assert car1.max_speed == 100
    assert car1.fuel_level == 100

def test_accelerate_changes():
    car1 = Car("Honda", "Jazz", "HK11ABC", 5, 4, 1.2, 0, 100, 100)
    car1.accelerate(50)
    assert car1.current_speed == 50


def test_brake_changes():
    car1 = Car("Honda", "Jazz", "HK11ABC", 5, 4, 1.2, 20, 100, 100)
    car1.brake(10)
    assert car1.current_speed == 10


def test_refuel_changes():
    car1 = Car("Honda", "Jazz", "HK11ABC", 5, 4, 1.2, 0, 100, 50)
    car1.refuel(30)
    assert car1.fuel_level == 80


def test_max_speed_limit():
    car1 = Car("Honda", "Jazz", "HK11ABC", 5, 4, 1.2, 20, 100, 100)
    car1.accelerate(81)
    assert car1.current_speed == car1.max_speed


def test_too_slow_returns_false():
    car1 = Car("Honda", "Jazz", "HK11ABC", 5, 4, 1.2, 20, 100, 100)
    car1.brake(21)
    assert car1.current_speed == 0


def test_max_fuel_limit():
    car1 = Car("Honda", "Jazz", "HK11ABC", 5, 4, 1.2, 20, 100, 80)
    car1.refuel(30)
    assert car1.fuel_level == 100

