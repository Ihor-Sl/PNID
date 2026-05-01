"""Утиліти для роботи з рядками."""

from __future__ import annotations


class StringUtils:
    """Набір статичних методів для роботи з рядками."""

    @staticmethod
    def reverse(text: str) -> str:
        """Повертає рядок у зворотному порядку."""
        return text[::-1]

    @staticmethod
    def is_palindrome(text: str) -> bool:
        """Перевіряє, чи є рядок паліндромом (без урахування регістру та пробілів)."""
        cleaned = "".join(text.lower().split())
        return cleaned == cleaned[::-1]

    @staticmethod
    def count_vowels(text: str) -> int:
        """Підраховує кількість голосних в рядку (англ. + укр.)."""
        vowels = set("aeiouAEIOUаеиіїоуюяєАЕИІЇОУЮЯЄ")
        return sum(1 for ch in text if ch in vowels)

    @staticmethod
    def word_count(text: str) -> int:
        """Підраховує кількість слів у рядку."""
        return len(text.split())

    @staticmethod
    def capitalize_words(text: str) -> str:
        """Робить першу літеру кожного слова великою."""
        return " ".join(word.capitalize() for word in text.split())

    @staticmethod
    def remove_duplicates(text: str) -> str:
        """Видаляє повторювані символи, зберігаючи порядок."""
        seen: set[str] = set()
        result: list[str] = []
        for ch in text:
            if ch not in seen:
                seen.add(ch)
                result.append(ch)
        return "".join(result)
