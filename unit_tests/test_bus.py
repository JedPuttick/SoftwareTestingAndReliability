import pytest
import bus
from person import Person


@pytest.fixture
def default_person():
    return Person("abc", 30, "Male", "def")


@pytest.fixture
def infant_person():
    return Person("abc", 2, "Male", "def")


@pytest.fixture
def student_person():
    return Person("abc", 18, "Male", "student")


def test_normal_ticket(default_person):
    assert bus.ticket_price(default_person) == 4


def test_infant_ticket(infant_person):
    assert bus.ticket_price(infant_person) == 0


def test_student_ticket(student_person):
    assert bus.ticket_price(student_person) == 2


def test_senior_ticket():
    senior = Person("abc", 65, "Male", "def")
    assert bus.ticket_price(senior) == 0


