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


if __name__ == "__main__":
    try:
        okno = tk.Tk()
        okno.title("Generator hasła")
        okno.geometry("420x480")
        okno.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("red.Horizontal.TProgressbar", background="red")
        style.configure("orange.Horizontal.TProgressbar", background="orange")
        style.configure("green.Horizontal.TProgressbar", background="green")

        historia = []

        # --- stan menu (POPRAWKA zamiast nonlocal) ---
        panel_otwarty = tk.BooleanVar(value=False)

        # --- GŁÓWNY FRAME ---
        main = ttk.Frame(okno, padding=15)
        main.pack(fill="both", expand=True)

        # --- MENU ☰ ---
        def toggle_historia():
            panel_otwarty.set(not panel_otwarty.get())

            if panel_otwarty.get():
                historia_frame.place(x=0, y=40, width=200, height=400)
                odswiez_historie()
            else:
                historia_frame.place_forget()

        ttk.Button(okno, text="Historia", width=7, command=toggle_historia).place(x=5, y=5)

        # --- PANEL HISTORII ---
        historia_frame = tk.Frame(okno, bg="#f0f0f0", bd=2, relief="raised")

        listbox = tk.Listbox(historia_frame)
        listbox.pack(fill="both", expand=True)

        def odswiez_historie():
            listbox.delete(0, tk.END)
            for h in historia:
                listbox.insert(tk.END, h)

        def kopiuj_z_listy(event):
            sel = listbox.curselection()
            if sel:
                haslo = listbox.get(sel[0])
                okno.clipboard_clear()
                okno.clipboard_append(haslo)
                okno.update()

        listbox.bind("<<ListboxSelect>>", kopiuj_z_listy)

        # --- UI ---
        ttk.Label(main, text="Generator hasła", font=("Segoe UI", 14, "bold")).pack(pady=10)

        settings = ttk.LabelFrame(main, text="Ustawienia", padding=10)
        settings.pack(fill="x")

        ttk.Label(settings, text="Długość:").grid(row=0, column=0)

        dlugosc_entry = ttk.Entry(settings, width=5, justify="center")
        dlugosc_entry.insert(0, "10")
        dlugosc_entry.grid(row=0, column=1)

        uzyj_cyfr_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(settings, text="Cyfry", variable=uzyj_cyfr_var).grid(row=1, column=0)

        uzyj_specjalnych_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(settings, text="Specjalne", variable=uzyj_specjalnych_var).grid(row=1, column=1)

        def zmiana(v):
            dlugosc_entry.delete(0, tk.END)
            dlugosc_entry.insert(0, str(int(float(v))))

        slider = ttk.Scale(settings, from_=4, to=32, orient="horizontal", command=zmiana)
        slider.set(10)
        slider.grid(row=2, column=0, columnspan=2, sticky="ew")

        def aktualizuj_slider(event):
            try:
                w = int(dlugosc_entry.get())
                w = max(4, min(32, w))
                slider.set(w)
                dlugosc_entry.delete(0, tk.END)
                dlugosc_entry.insert(0, str(w))
            except ValueError:
                pass

        dlugosc_entry.bind("<KeyRelease>", aktualizuj_slider)

        # --- HASŁO ---
        output = ttk.LabelFrame(main, text="Hasło", padding=10)
        output.pack(fill="x", pady=10)

        haslo_var = tk.StringVar(value="Kliknij Generuj")

        ttk.Entry(output, textvariable=haslo_var, font=("Consolas", 12), justify="center").pack(fill="x")

        sila_label = ttk.Label(output, text="")
        sila_label.pack(pady=5)

        progress = ttk.Progressbar(output, length=250, mode="determinate", maximum=100)
        progress.pack(pady=5)

        status_label = ttk.Label(main, text="")
        status_label.pack()

        def dodaj_do_historii(haslo):
            historia.insert(0, haslo)
            if len(historia) > 10:
                historia.pop()

        # --- FUNKCJE ---
        def generuj():
            try:
                dlugosc = int(dlugosc_entry.get())

                haslo = generator_hasel(
                    dlugosc_hasla=dlugosc,
                    uzyj_cyfr=uzyj_cyfr_var.get(),
                    uzyj_specjalnych=uzyj_specjalnych_var.get()
                )

                haslo_var.set(haslo)

                sila, wartosc, kolor = ocena_sily_hasla(haslo)

                sila_label.config(text=f"Siła hasła: {sila}", foreground=kolor)
                progress["value"] = wartosc

                if kolor == "red":
                    progress.config(style="red.Horizontal.TProgressbar")
                elif kolor == "orange":
                    progress.config(style="orange.Horizontal.TProgressbar")
                else:
                    progress.config(style="green.Horizontal.TProgressbar")

                dodaj_do_historii(haslo)

                if panel_otwarty.get():
                    odswiez_historie()

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

        btns = ttk.Frame(main)
        btns.pack(pady=10)

        ttk.Button(btns, text="Generuj", command=generuj).grid(row=0, column=0, padx=5)
        ttk.Button(btns, text="Kopiuj", command=kopiuj_haslo).grid(row=0, column=1, padx=5)

        okno.mainloop()

    except tk.TclError:
        print("Błąd ekranu")
