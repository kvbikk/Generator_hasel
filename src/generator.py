# import random
# import string

# def generate_password(length=12, use_digits=True, use_special=True):
#     """
#     Generuje losowe hasło o określonej długości i złożoności.
#     """
#     if length < 4:
#         raise ValueError("Hasło musi mieć co najmniej 4 znaki dla zachowania bezpieczeństwa.")

#     # Podstawowa pula: małe i wielkie litery
#     chars = string.ascii_letters
    
#     if use_digits:
#         chars += string.digits
#     if use_special:
#         chars += string.punctuation

#     # Generowanie hasła
#     password = ''.join(random.choice(chars) for _ in range(length))
#     return password

# if __name__ == "__main__":
#     # Przykład użycia przy ręcznym uruchomieniu: python src/generator.py
#     try:
#         print(f"Wygenerowane hasło (16 znaków): {generate_password(16)}")
#     except ValueError as e:
#         print(f"Błąd: {e}")




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