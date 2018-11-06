from src.cli.roman import roman_to_int, int_to_roman
import pytest

roman = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI",
         "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
         "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII",
         "XXIX", "XXX", "XXXI")
numbr = range(1, len(roman))


@pytest.mark.parametrize("Takes number, gives roman", *zip(numbr, roman))
def test_number_roman(n, expected):
    assert int_to_roman(n) == expected


@pytest.mark.parametrize("Takes roman, gives number", *zip(numbr, roman))
def test_roman_number(n, expected):
    assert int_to_roman(n) == expected
