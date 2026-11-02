
import pytest

from train_fare import base_fare, concession, tatkal_charge


# ==========================================
# BASE FARE - BRANCH TESTING
# ==========================================

def test_valid_class_sleeper():
    assert base_fare("SL", 500) == 500


def test_valid_class_ac():
    assert base_fare("3A", 100) == 200


def test_valid_class_ac_first():
    assert base_fare("1A", 100) == 500


def test_invalid_class_branch():
    with pytest.raises(ValueError, match="unknown class"):
        base_fare("5A", 100)


def test_valid_distance_branch():
    assert base_fare("SL", 100) == 100


def test_zero_distance_branch():
    with pytest.raises(ValueError, match="invalid distance"):
        base_fare("SL", 0)


def test_negative_distance_branch():
    with pytest.raises(ValueError, match="invalid distance"):
        base_fare("3A", -50)


def test_fare_below_minimum_branch():
    assert base_fare("SL", 10) == 50


def test_fare_above_minimum_branch():
    assert base_fare("2A", 100) == 300


# ==========================================
# CONCESSION - BRANCH TESTING
# ==========================================

def test_tatkal_true_branch():
    assert concession(65, "F", True) == 0


def test_tatkal_false_branch():
    assert concession(30, "M", False) == 0


def test_age_below_five_branch():
    assert concession(4, "M", False) == 100


def test_age_five_boundary():
    assert concession(5, "M", False) == 50


def test_age_twelve_boundary():
    assert concession(12, "F", False) == 50


def test_age_above_twelve_branch():
    assert concession(30, "F", False) == 0


def test_senior_age_branch():
    assert concession(60, "M", False) == 40


def test_below_senior_age_branch():
    assert concession(59, "M", False) == 0


def test_senior_female_branch():
    assert concession(65, "F", False) == 50


def test_senior_non_female_branch():
    assert concession(65, "M", False) == 40


# ==========================================
# TATKAL CHARGE - BRANCH TESTING
# ==========================================

def test_sleeper_class_branch():
    assert tatkal_charge("SL", 1000) == 100


def test_non_sleeper_class_branch():
    assert tatkal_charge("3A", 1000) == 300


def test_charge_above_400_branch():
    assert tatkal_charge("3A", 2000) == 400


def test_charge_below_100_branch():
    assert tatkal_charge("3A", 100) == 100


def test_charge_equal_to_100_branch():
    assert tatkal_charge("3A", 100) == 100


def test_charge_within_limits_branch():
    assert tatkal_charge("SL", 2000) == 200
