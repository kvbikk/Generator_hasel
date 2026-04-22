import random
import string
import tkinter as tk
from tkinter import ttk


def generator_hasel(dlugosc_hasla=10, uzyj_cyfr=True, uzyj_specjalnych=True):
    znaki = string.ascii_letters
    if uzyj_cyfr:
        znaki += string.digits
    if uzyj_specjalnych:
        znaki += string.punctuation

    return "".join(random.choice(znaki) for _ in range(dlugosc_hasla))


if __name__ == "__main__":
    try:
        okno = tk.Tk()
        okno.title("Generator hasła")
        okno.geometry("360x420")
        okno.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")

        # --- GŁÓWNA RAMKA ---
        main = ttk.Frame(okno, padding=15)
        main.pack(fill="both", expand=True)

        ttk.Label(main, text="🔐 Generator hasła", font=("Segoe UI", 14, "bold")).pack(pady=(0, 10))

        # --- USTAWIENIA ---
        settings = ttk.LabelFrame(main, text="Ustawienia", padding=10)
        settings.pack(fill="x", pady=5)

        ttk.Label(settings, text="Długość hasła:").grid(row=0, column=0, sticky="w")

        dlugosc_entry = ttk.Entry(settings, width=5, justify="center")
        dlugosc_entry.insert(0, "10")
        dlugosc_entry.grid(row=0, column=1, padx=5)

        uzyj_cyfr_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(settings, text="Cyfry", variable=uzyj_cyfr_var).grid(row=1, column=0, sticky="w")

        uzyj_specjalnych_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(settings, text="Znaki specjalne", variable=uzyj_specjalnych_var).grid(row=1, column=1, sticky="w")

        # --- SLIDER ---
        def zmiana(v):
            dlugosc_entry.delete(0, tk.END)
            dlugosc_entry.insert(0, str(int(float(v))))

        slider = ttk.Scale(settings, from_=4, to=32, orient="horizontal", command=zmiana)
        slider.set(10)
        slider.grid(row=2, column=0, columnspan=2, sticky="ew", pady=5)

        # --- ENTRY -> SLIDER ---
        def aktualizuj_slider(event):
            try:
                wartosc = int(dlugosc_entry.get())
                wartosc = max(4, min(32, wartosc))

                slider.set(wartosc)
                dlugosc_entry.delete(0, tk.END)
                dlugosc_entry.insert(0, str(wartosc))
            except ValueError:
                pass

        dlugosc_entry.bind("<KeyRelease>", aktualizuj_slider)

        # --- HASŁO ---
        output = ttk.LabelFrame(main, text="Twoje hasło", padding=10)
        output.pack(fill="x", pady=10)

        haslo_var = tk.StringVar(value="Kliknij Generuj")

        haslo_entry = ttk.Entry(output, textvariable=haslo_var, font=("Consolas", 12), justify="center")
        haslo_entry.pack(fill="x", padx=5, pady=5)

        status_label = ttk.Label(main, text="")
        status_label.pack()

        # --- FUNKCJE ---
        def generuj():
            try:
                dlugosc = int(dlugosc_entry.get())
                nowe_haslo = generator_hasel(
                    dlugosc_hasla=dlugosc,
                    uzyj_cyfr=uzyj_cyfr_var.get(),
                    uzyj_specjalnych=uzyj_specjalnych_var.get()
                )
                haslo_var.set(nowe_haslo)
                status_label.config(text="")
            except ValueError:
                status_label.config(text="❌ Błędna wartość")

        def kopiuj_haslo():
            haslo = haslo_var.get()
            if haslo and haslo != "Kliknij Generuj":
                okno.clipboard_clear()
                okno.clipboard_append(haslo)
                okno.update()

                status_label.config(text="✔ Skopiowano!")
                okno.after(1500, lambda: status_label.config(text=""))

        # --- PRZYCISKI ---
        btn_frame = ttk.Frame(main)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Generuj", command=generuj).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Kopiuj", command=kopiuj_haslo).grid(row=0, column=1, padx=5)

        okno.mainloop()

    except tk.TclError:
        print("Błąd ekranu")
