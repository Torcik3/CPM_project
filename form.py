import tkinter as tk
from tkinter import ttk

class FormularzCPM:
    def __init__(self, master):
        self.lp_counter = 1
        self.master = master
        self.setup_gui()

    def setup_gui(self):
        # Ramki
        self.lewa_ramka = tk.Frame(self.master)
        self.lewa_ramka.pack(side="left", fill="both", expand=False, padx=10, pady=10)

        self.prawa_ramka = tk.Frame(self.master)
        self.prawa_ramka.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Pola formularza
        tk.Label(self.lewa_ramka, text="Nazwa zdarzenia:").pack(anchor="w", pady=(0, 2))
        self.nazwa_zdarzenia = tk.Entry(self.lewa_ramka, width=30)
        self.nazwa_zdarzenia.pack(anchor='w', pady=(0, 10))

        tk.Label(self.lewa_ramka, text="Czas trwania zdarzenia (dni):").pack(anchor="w", pady=(0, 2))
        self.t_zdarzenia = tk.Entry(self.lewa_ramka, width=30)
        self.t_zdarzenia.pack(anchor='w', pady=(0, 10))

        tk.Label(self.lewa_ramka, text="Następstwo od:").pack(anchor="w", pady=(0, 2))
        self.nastepstwo_od = tk.Entry(self.lewa_ramka, width=30)
        self.nastepstwo_od.pack(anchor='w', pady=(0, 10))

        tk.Label(self.lewa_ramka, text="Następstwo do:").pack(anchor="w", pady=(0, 2))
        self.nastepstwo_do = tk.Entry(self.lewa_ramka, width=30)
        self.nastepstwo_do.pack(anchor='w', pady=(0, 10))

        tk.Button(self.lewa_ramka, text="Dodaj", command=self.dodanie_do_tabeli).pack(anchor="w", pady=(10, 0))
        tk.Button(self.lewa_ramka, text="Usuń zaznaczony", command=self.usun_zaznaczony).pack(anchor="w", pady=(5, 0))

        # Tabela
        kolumny = ("Lp.", "Nazwa zdarzenia", "Czas trwania zdarzenia", "Nastepstwa")
        self.tabela = ttk.Treeview(self.prawa_ramka, columns=kolumny, show="headings")

        for kolumna in kolumny:
            self.tabela.heading(kolumna, text=kolumna)
            self.tabela.column(kolumna, anchor=tk.CENTER)

        self.tabela.pack(fill="both", expand=True)


    def dodanie_do_tabeli(self):
        text_nazwa = self.nazwa_zdarzenia.get()
        text_czas_zd = self.t_zdarzenia.get()
        text_nast_od = self.nastepstwo_od.get()
        text_nast_do = self.nastepstwo_do.get()

        nastepstwa = f"{text_nast_od} - {text_nast_do}"

        self.tabela.insert("", "end", values=(self.lp_counter, text_nazwa, text_czas_zd, nastepstwa))
        self.lp_counter += 1

        self.nazwa_zdarzenia.delete(0, tk.END)
        self.t_zdarzenia.delete(0, tk.END)
        self.nastepstwo_od.delete(0, tk.END)
        self.nastepstwo_do.delete(0, tk.END)

    def usun_zaznaczony(self):
        wybrane = self.tabela.selection()
        for item in wybrane:
            self.tabela.delete(item)

    def pobierz_dane(self):
        dane = []
        for item in self.tabela.get_children():
            dane.append(self.tabela.item(item, "values"))
        return dane
