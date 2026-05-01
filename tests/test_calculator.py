"""Тести для класу Calculator."""

import pytest

from src.calculator import Calculator


@pytest.fixture
def calc() -> Calculator:
    """Фікстура, що створює новий екземпляр калькулятора."""
    return Calculator()


class TestAddition:
    def test_add_positive_numbers(self, calc: Calculator) -> None:
        assert calc.add(2, 3) == 5

    def test_add_negative_numbers(self, calc: Calculator) -> None:
        assert calc.add(-5, -3) == -8

    def test_add_zero(self, calc: Calculator) -> None:
        assert calc.add(0, 7) == 7

    def test_add_floats(self, calc: Calculator) -> None:
        assert calc.add(0.1, 0.2) == pytest.approx(0.3)


class TestSubtraction:
    def test_subtract_positive(self, calc: Calculator) -> None:
        assert calc.subtract(10, 4) == 6

    def test_subtract_negative_result(self, calc: Calculator) -> None:
        assert calc.subtract(3, 8) == -5

    def test_subtract_zero(self, calc: Calculator) -> None:
        assert calc.subtract(5, 0) == 5


class TestMultiplication:
    def test_multiply_positive(self, calc: Calculator) -> None:
        assert calc.multiply(6, 7) == 42

    def test_multiply_by_zero(self, calc: Calculator) -> None:
        assert calc.multiply(100, 0) == 0

    def test_multiply_negative(self, calc: Calculator) -> None:
        assert calc.multiply(-3, 4) == -12


class TestDivision:
    def test_divide_normal(self, calc: Calculator) -> None:
        assert calc.divide(20, 5) == 4

    def test_divide_floats(self, calc: Calculator) -> None:
        assert calc.divide(1, 4) == 0.25

    def test_divide_by_zero_raises(self, calc: Calculator) -> None:
        with pytest.raises(ValueError, match="Ділення на нуль"):
            calc.divide(10, 0)


class TestPower:
    @pytest.mark.parametrize(
        "base,exponent,expected",
        [
            (2, 10, 1024),
            (5, 0, 1),
            (3, 2, 9),
            (2, -1, 0.5),
        ],
    )
    def test_power_cases(
        self, calc: Calculator, base: float, exponent: float, expected: float
    ) -> None:
        assert calc.power(base, exponent) == expected


class TestHistory:
    def test_history_records_operations(self, calc: Calculator) -> None:
        calc.add(1, 2)
        calc.multiply(3, 4)
        history = calc.get_history()
        assert len(history) == 2
        assert "1 + 2 = 3" in history[0]
        assert "3 * 4 = 12" in history[1]

    def test_clear_history(self, calc: Calculator) -> None:
        calc.add(1, 1)
        calc.clear_history()
        assert calc.get_history() == []

    def test_history_is_independent_copy(self, calc: Calculator) -> None:
        calc.add(1, 1)
        history = calc.get_history()
        history.append("hacked")
        assert len(calc.get_history()) == 1
