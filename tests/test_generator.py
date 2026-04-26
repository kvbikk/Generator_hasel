import string
import pytest
from src.generator import generator_hasel
from src.logika import generator_hasel


# zmieniamy liczbę w funkcji generator_hasel
def test_dlugosc_domyslna():
    haslo = generator_hasel()
    assert len(haslo) == 10


# dlugosc == moja_dlugosc, zmieniamy tu i w pliku generator.py
def test_dlugosc_zadana():
    dlugosc = 15
    haslo = generator_hasel(dlugosc_hasla=dlugosc)
    assert len(haslo) == dlugosc


# Przy zmianie na True, wywala błąd
def test_czy_zawiera_tylko_litery():
    haslo = generator_hasel(
        dlugosc_hasla=10, uzyj_cyfr=False, uzyj_specjalnych=False
    )
    for i in haslo:
        assert i in string.ascii_letters
        print(haslo)


# generuje 2 hasła i sprawdza czy się różnią
def test_czy_sie_nie_powtarza():
    haslo1 = generator_hasel()
    haslo2 = generator_hasel()
    assert haslo1 != haslo2
