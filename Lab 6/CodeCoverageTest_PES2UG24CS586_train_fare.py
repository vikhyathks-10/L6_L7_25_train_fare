
import pytest

from train_fare import base_fare, concession, tatkal_charge


# ==========================================
# BASE FARE TEST CASES
# ==========================================

def test_valid_sleeper_fare():
    assert base_fare("SL", 500) == 500


def test_valid_ac_fare():
    assert base_fare("3A", 100) == 200


def test_invalid_travel_class():
    with pytest.raises(ValueError, match="unknown class"):
        base_fare("5A", 100)


def test_invalid_zero_distance():
    with pytest.raises(ValueError, match="invalid distance"):
        base_fare("SL", 0)


def test_invalid_negative_distance():
    with pytest.raises(ValueError, match="invalid distance"):
        base_fare("SL", -10)


def test_minimum_base_fare():
    assert base_fare("SL", 10) == 50


# ==========================================
# CONCESSION TEST CASES
# ==========================================

def test_tatkal_no_concession():
    assert concession(5, "F", True) == 0


def test_child_below_five():
    assert concession(4, "M", False) == 100


def test_child_age_five():
    assert concession(5, "M", False) == 50


def test_child_age_twelve():
    assert concession(12, "F", False) == 50


def test_adult_no_concession():
    assert concession(30, "M", False) == 0


def test_senior_citizen_female():
    assert concession(60, "F", False) == 50


def test_senior_citizen_male():
    assert concession(65, "M", False) == 40


# ==========================================
# TATKAL CHARGE TEST CASES
# ==========================================

def test_sleeper_tatkal_charge():
    assert tatkal_charge("SL", 500) == 100


def test_ac_tatkal_charge():
    assert tatkal_charge("3A", 500) == 150


def test_tatkal_minimum_charge():
    assert tatkal_charge("3A", 100) == 100


def test_tatkal_maximum_charge():
    assert tatkal_charge("3A", 2000) == 400


def test_tatkal_charge_within_limits():
    assert tatkal_charge("SL", 2000) == 200

