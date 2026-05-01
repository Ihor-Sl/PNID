"""Простий калькулятор з базовими арифметичними операціями."""

from __future__ import annotations

# Some changes
class Calculator:
    """Калькулятор, що підтримує основні арифметичні операції."""

    def __init__(self) -> None:
        self.history: list[str] = []

    def add(self, a: float, b: float) -> float:
        """Повертає суму двох чисел."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        """Повертає різницю двох чисел."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """Повертає добуток двох чисел."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        """Повертає частку двох чисел.

        Викидає ValueError при діленні на нуль.
        """
        if b == 0:
            raise ValueError("Ділення на нуль неможливе")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def power(self, base: float, exponent: float) -> float:
        """Підносить число до степеня."""
        result = base**exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result

    def clear_history(self) -> None:
        """Очищає історію операцій."""
        self.history.clear()

    def get_history(self) -> list[str]:
        """Повертає копію історії операцій."""
        return list(self.history)
