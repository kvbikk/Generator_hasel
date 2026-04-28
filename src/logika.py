import random
import string


def generator_hasel(dlugosc_hasla=10, uzyj_cyfr=True, uzyj_specjalnych=True, uzyj_duzych=True):
    znaki = string.ascii_lowercase
    if uzyj_duzych:
        znaki += string.ascii_uppercase
    if uzyj_cyfr:
        znaki += string.digits
    if uzyj_specjalnych:
        znaki += string.punctuation
    if not znaki:
        znaki = string.ascii_lowercase

    return "".join(random.choice(znaki) for _ in range(dlugosc_hasla))


def ocena_sily_hasla(haslo):
    sila = 0
    if len(haslo) >= 8:
        sila += 1
    if len(haslo) >= 12:
        sila += 1
    if any(c.isdigit() for c in haslo):
        sila += 1
    if any(c in string.punctuation for c in haslo):
        sila += 1
    if any(c.islower() for c in haslo) and any(c.isupper() for c in haslo):
        sila += 1

    if sila <= 2:
        return "Słabe", 33, "red"
    elif sila == 3:
        return "Średnie", 66, "orange"
    else:
        return "Mocne", 100, "green"
