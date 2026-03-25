import random
import string


def generator_hasel(dlugosc_hasla=10):
    znaki = string.ascii_letters + string.digits + string.punctuation
    haslo = ""
    for i in range(dlugosc_hasla):
        losowe_znaki = random.choice(znaki)
        haslo += losowe_znaki
    return haslo

moja_dlugosc = None

if moja_dlugosc is None:
    nowe_haslo = generator_hasel()
    wyswietl_dlugosc = 10
else:
    nowe_haslo = generator_hasel(dlugosc_hasla=moja_dlugosc)
    wyswietl_dlugosc = moja_dlugosc

print(f"Hasło składa się z: {wyswietl_dlugosc} znaków")
print(f"Twoje nowe hasło to: {nowe_haslo}")