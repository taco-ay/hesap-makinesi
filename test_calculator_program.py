import pytest
from calculate.calculator_program import calculate

def test_addition():
    assert calculate(2, 3, '+') == 5

def test_subtraction():
    assert calculate(10, 4, '-') == 6

def test_multiplication():
    assert calculate(3, 5, '*') == 15

def test_division():
    assert calculate(8, 2, '/') == 4

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(5, 0, '/')

def test_unknown_operation():
    with pytest.raises(ValueError):
        calculate(2, 3, '%')