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
        losowy_znak = random.choice(znaki)
        haslo += losowy_znak
    return haslo


if __name__ == "__main__":
    try:
        okno = tkinter.Tk()
        okno.title("Generator hasła")
        okno.geometry("300x380")

        tkinter.Label(okno, text="Długość hasła:").pack()

        dlugosc_entry = tkinter.Entry(okno)
        dlugosc_entry.insert(0, "10")
        dlugosc_entry.pack()

        uzyj_cyfr_var = tkinter.BooleanVar(value=True)
        tkinter.Checkbutton(okno, text="Użyj cyfr", variable=uzyj_cyfr_var).pack()

        uzyj_specjalnych_var = tkinter.BooleanVar(value=True)
        tkinter.Checkbutton(okno, text="Użyj znaków specjalnych", variable=uzyj_specjalnych_var).pack()

        haslo_label = tkinter.Label(okno, text="", font=("Verdana", 16))
        haslo_label.pack(pady=10)

        status_label = tkinter.Label(okno, text="", fg="green")
        status_label.pack()

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
                uzyj_specjalnych=uzyj_specjalnych_var.get()
            )
            haslo_label.config(text=nowe_haslo)
            status_label.config(text="")  # reset ✔

        def kopiuj_haslo():
            haslo = haslo_label.cget("text")
            if haslo:
                okno.clipboard_clear()
                okno.clipboard_append(haslo)
                okno.update()

                status_label.config(text="✔ Skopiowano!")
                okno.after(1500, lambda: status_label.config(text=""))

        tkinter.Button(okno, text="Generuj", command=generuj).pack(pady=5)
        tkinter.Button(okno, text="Kopiuj hasło", command=kopiuj_haslo).pack(pady=5)

        okno.mainloop()

    except tkinter.TclError:
        print("Błąd ekranu")
