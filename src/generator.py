import tkinter as tk
import customtkinter as ctk
from src.logika import generator_hasel, ocena_sily_hasla


KOLORY = {
    "surface":  ("#EBEBEB", "#161920"),
    "border":   ("#D4D4D4", "#2a2f3f"),
    "accent":   ("#77CF65", "#00e5a0"),
    "hover":    ("#77CF65", "#00ffb2"),
    "text":     ("#1A1A1A", "#e8eaf2"),
    "muted":    ("#666666", "#5a607a"),
    "surf2":    ("#D9D9D9", "#1e2230"),
    "btn_text": ("#FFFFFF", "#0d0f14"),
}


class App:
    def __init__(self):
        self.okno = ctk.CTk()
        ctk.set_appearance_mode("dark")
        self.okno.title("Generator hasła")
        self.okno.geometry("440x550")
        self.okno.resizable(False, False)

        self.biezace_haslo = ""
        self.historia = []

        self.ui()

    def zmien_tryb(self):
        if self.switch.get() == 1:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    def ui(self):
        # Nagłówek i tryb
        nagl = ctk.CTkFrame(self.okno, fg_color=KOLORY["surface"], corner_radius=16)
        nagl.pack(fill="x", padx=20, pady=(20, 10))

        self.switch = ctk.CTkSwitch(nagl, text="Tryb", command=self.zmien_tryb, width=50)
        self.switch.select()
        self.switch.pack(side="right", padx=15, pady=10)

        ctk.CTkLabel(
            nagl, text="Generator Haseł", font=("Segoe UI", 17, "bold"), text_color=KOLORY["text"]
        ).pack(side="left", padx=15, pady=10)

        # Pole wyniku
        haslo_frame = ctk.CTkFrame(
            self.okno, fg_color=KOLORY["surface"], corner_radius=14, border_width=1, border_color=KOLORY["border"]
        )
        haslo_frame.pack(fill="x", padx=20, pady=10)

        self.wynik_entry = ctk.CTkEntry(
            haslo_frame,
            font=("Consolas", 18),
            fg_color="transparent",
            text_color=KOLORY["text"],
            border_width=0,
            justify="center"
        )
        self.wynik_entry.pack(fill="x", padx=10, pady=(15, 5))
        self.wynik_entry.insert(0, "Kliknij Generuj")

        self.kopiuj_btn = ctk.CTkButton(
            haslo_frame, text="Kopiuj", fg_color=KOLORY["surf2"], hover_color=KOLORY["border"],
            text_color=KOLORY["text"], border_width=1, border_color=KOLORY["border"],
            corner_radius=8, command=self.kopiuj
        )
        self.kopiuj_btn.pack(pady=(5, 15))

        # Slider Długości
        slider_label_frame = ctk.CTkFrame(self.okno, fg_color="transparent")
        slider_label_frame.pack(fill="x", padx=30, pady=(10, 0))

        ctk.CTkLabel(slider_label_frame, text="Długość hasła:", font=("Segoe UI", 12), text_color=KOLORY["text"]).pack(side="left")
        self.wartosc_label = ctk.CTkLabel(
            slider_label_frame, text="12", font=("Segoe UI", 13, "bold"), text_color=KOLORY["accent"]
        )
        self.wartosc_label.pack(side="right")

        self.dlugosc_slider = ctk.CTkSlider(
            self.okno, from_=4, to=32, number_of_steps=28,
            command=self.slider_event, button_color=KOLORY["accent"], progress_color=KOLORY["accent"]
        )
        self.dlugosc_slider.set(12)
        self.dlugosc_slider.pack(fill="x", padx=30, pady=10)

        # Checkboxy
        self.uzyj_duzych_var = ctk.BooleanVar(value=True)
        self.uzyj_cyfr_var = ctk.BooleanVar(value=True)
        self.uzyj_specjalnych_var = ctk.BooleanVar(value=True)

        check_frame = ctk.CTkFrame(self.okno, fg_color="transparent")
        check_frame.pack(pady=5)

        params = {"text_color": KOLORY["text"], "fg_color": KOLORY["accent"], "hover_color": KOLORY["hover"]}
        ctk.CTkCheckBox(check_frame, text="Duże litery", variable=self.uzyj_duzych_var, **params).pack(side="left", padx=8)
        ctk.CTkCheckBox(check_frame, text="Cyfry", variable=self.uzyj_cyfr_var, **params).pack(side="left", padx=8)
        ctk.CTkCheckBox(check_frame, text="Symbole", variable=self.uzyj_specjalnych_var, **params).pack(side="left", padx=8)

        # Pasek siły
        self.sila_bar = ctk.CTkProgressBar(self.okno)
        self.sila_bar.set(0)
        self.sila_bar.pack(fill="x", padx=40, pady=(15, 0))

        self.sila_label = ctk.CTkLabel(self.okno, text="Siła: -", font=("Segoe UI", 11), text_color=KOLORY["text"])
        self.sila_label.pack()

        # Przyciski
        btn_row = ctk.CTkFrame(self.okno, fg_color="transparent")
        btn_row.pack(fill="x", padx=40, pady=(15, 20))

        self.hist_btn = ctk.CTkButton(
            btn_row, text="🕘 Historia", width=100, height=45,
            fg_color=KOLORY["surf2"], hover_color=KOLORY["border"], text_color=KOLORY["text"],
            border_width=1, border_color=KOLORY["border"], corner_radius=12,
            command=self.pokaz_historie
        )
        self.hist_btn.pack(side="left", padx=(0, 10))

        self.gen_btn = ctk.CTkButton(
            btn_row, text=" Generuj", height=45, command=self.generuj,
            fg_color=KOLORY["accent"], hover_color=KOLORY["hover"], text_color=KOLORY["btn_text"],
            font=("Segoe UI", 14, "bold"), corner_radius=12
        )
        self.gen_btn.pack(side="left", fill="x", expand=True)

    def slider_event(self, value):
        self.wartosc_label.configure(text=str(int(value)))

    def generuj(self):
        dlugosc = int(self.dlugosc_slider.get())
        haslo = generator_hasel(
            dlugosc_hasla=dlugosc,
            uzyj_duzych=self.uzyj_duzych_var.get(),
            uzyj_cyfr=self.uzyj_cyfr_var.get(),
            uzyj_specjalnych=self.uzyj_specjalnych_var.get()
        )
        self.biezace_haslo = haslo

        self.historia.insert(0, haslo)
        if len(self.historia) > 15:
            self.historia.pop()

        self.wynik_entry.delete(0, tk.END)
        self.wynik_entry.insert(0, haslo)

        napis, proc, kolor = ocena_sily_hasla(haslo)
        self.sila_bar.set(proc/100)
        self.sila_bar.configure(progress_color=kolor)
        self.sila_label.configure(text=f"Siła: {napis}", text_color=kolor)

    def kopiuj(self):
        if not self.biezace_haslo:
            return

        self.okno.clipboard_clear()
        self.okno.clipboard_append(self.biezace_haslo)
        self.okno.update()

        self.kopiuj_btn.configure(text="✔ Skopiowano!", text_color=KOLORY["accent"])
        self.okno.after(1500, lambda: self.kopiuj_btn.configure(text="Kopiuj", text_color=KOLORY["text"]))

    def pokaz_historie(self):
        okno_hist = ctk.CTkToplevel(self.okno)
        okno_hist.title("Historia")
        okno_hist.geometry("300x400")
        okno_hist.transient(self.okno)

        ctk.CTkLabel(
            okno_hist, text="Ostatnie hasła", font=("Segoe UI", 16, "bold"), text_color=KOLORY["text"]
        ).pack(pady=10)

        scroll = ctk.CTkScrollableFrame(okno_hist, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=10, pady=10)

        if not self.historia:
            ctk.CTkLabel(scroll, text="Brak wygenerowanych haseł.", text_color=KOLORY["muted"]).pack(pady=20)
            return

        for haslo in self.historia:
            ramka = ctk.CTkFrame(scroll, fg_color=KOLORY["surface"], corner_radius=8)
            ramka.pack(fill="x", pady=4)

            lbl = ctk.CTkLabel(ramka, text=haslo, font=("Consolas", 13), text_color=KOLORY["text"])
            lbl.pack(side="left", padx=10, pady=8)

            def kopiuj_z_historii(h=haslo):
                self.okno.clipboard_clear()
                self.okno.clipboard_append(h)
                self.okno.update()

            ctk.CTkButton(
                ramka, text="Kopiuj", width=50, height=24, fg_color=KOLORY["surf2"],
                hover_color=KOLORY["border"], text_color=KOLORY["text"], command=kopiuj_z_historii
            ).pack(side="right", padx=10)

try:
    if __name__ == "__main__":
        app = App()
        app.okno.mainloop()

except TclError:
    print("Brak środowiska graficznego")
