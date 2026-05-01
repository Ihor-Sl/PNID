"""Тести для класу StringUtils."""

import pytest

from src.string_utils import StringUtils


class TestReverse:
    def test_reverse_simple(self) -> None:
        assert StringUtils.reverse("hello") == "olleh"

    def test_reverse_empty(self) -> None:
        assert StringUtils.reverse("") == ""

    def test_reverse_unicode(self) -> None:
        assert StringUtils.reverse("привіт") == "тівирп"

    def test_reverse_single_char(self) -> None:
        assert StringUtils.reverse("a") == "a"


class TestPalindrome:
    @pytest.mark.parametrize(
        "text,expected",
        [
            ("racecar", True),
            ("hello", False),
            ("A man a plan a canal Panama", True),
            ("", True),
            ("a", True),
            ("ab", False),
        ],
    )
    def test_palindromes(self, text: str, expected: bool) -> None:
        assert StringUtils.is_palindrome(text) is expected


class TestCountVowels:
    def test_count_english_vowels(self) -> None:
        assert StringUtils.count_vowels("hello world") == 3

    def test_count_no_vowels(self) -> None:
        assert StringUtils.count_vowels("rhythm") == 0

    def test_count_ukrainian_vowels(self) -> None:
        assert StringUtils.count_vowels("привіт") == 2

    def test_count_mixed_case(self) -> None:
        assert StringUtils.count_vowels("AeIoU") == 5


class TestWordCount:
    @pytest.mark.parametrize(
        "text,expected",
        [
            ("hello world", 2),
            ("", 0),
            ("   ", 0),
            ("one", 1),
            ("a b c d e", 5),
        ],
    )
    def test_word_counts(self, text: str, expected: int) -> None:
        assert StringUtils.word_count(text) == expected


class TestCapitalizeWords:
    def test_capitalize_simple(self) -> None:
        assert StringUtils.capitalize_words("hello world") == "Hello World"

    def test_capitalize_single(self) -> None:
        assert StringUtils.capitalize_words("python") == "Python"

    def test_capitalize_empty(self) -> None:
        assert StringUtils.capitalize_words("") == ""


class TestRemoveDuplicates:
    def test_remove_duplicates_basic(self) -> None:
        assert StringUtils.remove_duplicates("aabbcc") == "abc"

    def test_preserves_order(self) -> None:
        assert StringUtils.remove_duplicates("banana") == "ban"

    def test_no_duplicates(self) -> None:
        assert StringUtils.remove_duplicates("abc") == "abc"

    def test_empty(self) -> None:
        assert StringUtils.remove_duplicates("") == ""
