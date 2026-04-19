import random
import string
import tkinter


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


if __name__ == "__main__":
    try:
        okno = tkinter.Tk()
        okno.title("Generator hasła")
        okno.geometry("300x300")

        tkinter.Label(okno, text="Długość hasła:").pack()
        dlugosc_entry = tkinter.Entry(okno)
        dlugosc_entry.insert(0, "10")
        dlugosc_entry.pack()

        uzyj_cyfr_var = tkinter.BooleanVar(value=False)
        tkinter.Checkbutton(okno, text="Użyj cyfr", variable=uzyj_cyfr_var).pack()

        uzyj_specjalnych_var = tkinter.BooleanVar(value=False)
        tkinter.Checkbutton(okno, text="Użyj specjalnych", variable=uzyj_specjalnych_var).pack()

        haslo_label = tkinter.Label(okno, text="",)
        haslo_label.pack()

        def zmiana(v):
            dlugosc_entry.delete(0, tkinter.END)
            dlugosc_entry.insert(0, str(int(float(v))))

        slider = tkinter.Scale(okno, from_=4, to=32, orient="horizontal", command=zmiana)
        slider.set(10)
        slider.pack()

        def generuj():
            dlugosc = int(dlugosc_entry.get())
            nowe_haslo = generator_hasel(
                dlugosc_hasla=dlugosc,
                uzyj_cyfr=uzyj_cyfr_var.get(),
                uzyj_specjalnych=uzyj_specjalnych_var.get())
            haslo_label.config(text=nowe_haslo, font=("Verdana", 20))

        moja_dlugosc = 15

        if moja_dlugosc is None:
            nowe_haslo = generator_hasel()
        else:
            nowe_haslo = generator_hasel(dlugosc_hasla=moja_dlugosc)

        print(f"Hasło składa się z: {len(nowe_haslo)} znaków")
        print(f"Twoje nowe hasło to: {nowe_haslo}")

        tkinter.Button(okno, text="Generuj", command=generuj).pack()
        okno.mainloop()
    except tkinter.TclError:
        print("Błąd ekranu")
