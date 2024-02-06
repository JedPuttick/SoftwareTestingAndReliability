import pytest
import speed_camera
from incident import Incident


def test_not_speeding():
    inc1 = Incident("AA11AAA", 70, 70)
    assert speed_camera.check_speed(inc1) == (False, False)


def test_slight_speeding():
    inc1 = Incident("AAA11AAA", 70, 71)
    assert speed_camera.check_speed(inc1) == (True, False)


def test_very_speeding():
    inc1 = Incident("AA11AAA", 70, 81)
    assert speed_camera.check_speed(inc1) == (True, True)
