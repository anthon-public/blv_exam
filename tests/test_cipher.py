import pytest

from app.cipher import CaesarCipher, SubstitutionCipher, cipher


def test_substitution_cipher_success():
    m = "AbCdE"
    n = {"A": "X", "C": "T", "E": "F"}

    substitution_cipher = SubstitutionCipher(n)
    encoded = substitution_cipher.cipher(m)
    assert encoded == "XbTdF"


def test_cipher_int_out_of_range():
    m = "AbCdE"
    n = -26

    caesar_cipher = CaesarCipher(n)

    with pytest.raises(ValueError):
        caesar_cipher.cipher(m)


def test_cipher_int_success():
    m = "AbCdE"
    n = 5

    caesar_cipher = CaesarCipher(n)
    encoded = caesar_cipher.cipher(m)
    assert encoded == "FgHiJ"


def test_cipher_int_with_special_character():
    m = "Ab(CdE%"
    n = -5

    caesar_cipher = CaesarCipher(n)
    encoded = caesar_cipher.cipher(m)
    assert encoded == "Vw(XyZ%"


def test_main_cipher_int():
    m = "AbCdE"
    n = 5

    encoded = cipher(m, n)
    assert encoded == "FgHiJ"


def test_main_cipher_dict():
    m = "AbCdE"
    n = {"A": "X", "C": "T", "E": "F"}

    encoded = cipher(m, n)
    assert encoded == "XbTdF"


def test_main_cipher_input_not_supported():
    m = "AbCdE"
    n = "not a valid input"

    with pytest.raises(ValueError):
        cipher(m, n)
