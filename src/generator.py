import random
import string


def generator_hasel(dlugosc_hasla=10, uzyj_cyfr=True, uzyj_specjalnych=True):
    znaki = string.ascii_letters
    if uzyj_cyfr:
        znaki += string.digits
    if uzyj_specjalnych:
        znaki += string.punctuation

    haslo = ""
    for i in range(dlugosc_hasla):
        losowy_znak = random.choice((znaki))
        haslo += losowy_znak
    return haslo


moja_dlugosc = 15


if moja_dlugosc is None:
    nowe_haslo = generator_hasel()
else:
    nowe_haslo = generator_hasel(dlugosc_hasla=moja_dlugosc)

print(f"Hasło składa się z: {len(nowe_haslo)} znaków")
print(f"Twoje nowe hasło to: {nowe_haslo}")
