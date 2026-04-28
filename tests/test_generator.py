import string
from src.logika import generator_hasel


def test_dlugosc_domyslna():
    haslo = generator_hasel()
    assert len(haslo) == 10


def test_dlugosc_zadana():
    dlugosc = 15
    haslo = generator_hasel(dlugosc_hasla=dlugosc)
    assert len(haslo) == dlugosc


def test_czy_zawiera_tylko_litery():
    haslo = generator_hasel(
        dlugosc_hasla=10, uzyj_cyfr=False, uzyj_specjalnych=False
    )
    for i in haslo:
        assert i in string.ascii_letters


def test_czy_sie_nie_powtarza():
    haslo1 = generator_hasel()
    haslo2 = generator_hasel()
    assert haslo1 != haslo2
