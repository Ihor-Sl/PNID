"""Точка входу для демонстрації роботи пакета."""

from src.calculator import Calculator
from src.string_utils import StringUtils


def main() -> None:
    """Демонструє роботу основних модулів."""
    calc = Calculator()
    print("=== Калькулятор ===")
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"20 / 5 = {calc.divide(20, 5)}")
    print(f"2 ^ 10 = {calc.power(2, 10)}")

    print("\n=== Утиліти для рядків ===")
    sample = "Привіт, світе!"
    print(f"Оригінал:        {sample}")
    print(f"Перевернутий:    {StringUtils.reverse(sample)}")
    print(f"Кількість слів:  {StringUtils.word_count(sample)}")
    print(f"Кількість голосних: {StringUtils.count_vowels(sample)}")
    print(
        f"Паліндром 'А роза упала на лапу Азора': "
        f"{StringUtils.is_palindrome('А роза упала на лапу Азора')}"
    )


if __name__ == "__main__":
    main()
