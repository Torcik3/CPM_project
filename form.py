import tkinter as tk
from tkinter import ttk

lp_counter = 1  # globalny licznik wierszy

def dodanie_do_tabeli():
    global lp_counter
    text_nazwa = nazwa_zdarzenia.get()
    text_czas_zd = t_zdarzenia.get()
    text_nast_od = nastepstwo_od.get()
    text_nast_do = nastepstwo_do.get()

    # Połączenie "następstwo od" i "do" w jedną kolumnę
    nastepstwa = f"{text_nast_od} - {text_nast_do}"

    # Dodanie do tabeli
    tabela.insert("", "end", values=(lp_counter, text_nazwa, text_czas_zd, nastepstwa))

    # Zwiększ licznik
    lp_counter += 1

    # Wyczyść pola po dodaniu
    nazwa_zdarzenia.delete(0, tk.END)
    t_zdarzenia.delete(0, tk.END)
    nastepstwo_od.delete(0, tk.END)
    nastepstwo_do.delete(0, tk.END)

def usun_zaznaczony():
    wybrane = tabela.selection()
    for item in wybrane:
        tabela.delete(item)

# Funkcja sprawdzająca czy wpisana wartość to liczba
def tylko_cyfry(tekst):
    return tekst.isdigit() or tekst == ""

# Tworzenie głównego okna
okno = tk.Tk()
okno.title("Formularz CPM")
okno.geometry("800x500")
okno.iconbitmap('C:\cymo\studia\S6\BOIL\CPM_project\logo_CPM.ico')

# Rejestracja walidacji
walidacja_cyfry = okno.register(tylko_cyfry)

# Główne ramki: lewa i prawa
lewa_ramka = tk.Frame(okno)
lewa_ramka.pack(side="left", fill="both", expand=False, padx=10, pady=10)

prawa_ramka = tk.Frame(okno)
prawa_ramka.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# --- Lewa strona (formularz) ---
etykieta_opisu = tk.Label(lewa_ramka, text="Nazwa zdarzenia:")
etykieta_opisu.pack(anchor="w", pady=(0, 2))
nazwa_zdarzenia = tk.Entry(lewa_ramka, width=30)
nazwa_zdarzenia.pack(anchor='w', pady=(0, 10))

etykieta_opisu = tk.Label(lewa_ramka, text="Czas trwania zdarzenia (dni):")
etykieta_opisu.pack(anchor="w", pady=(0, 2))
t_zdarzenia = tk.Entry(lewa_ramka, width=30, validate="key", validatecommand=(walidacja_cyfry, "%P"))
t_zdarzenia.pack(anchor='w', pady=(0, 10))

etykieta_opisu = tk.Label(lewa_ramka, text="Następstwo od:")
etykieta_opisu.pack(anchor="w", pady=(0, 2))
nastepstwo_od = tk.Entry(lewa_ramka, width=30, validate="key", validatecommand=(walidacja_cyfry, "%P"))
nastepstwo_od.pack(anchor='w', pady=(0, 10))

etykieta_opisu = tk.Label(lewa_ramka, text="Następstwo do:")
etykieta_opisu.pack(anchor="w", pady=(0, 2))
nastepstwo_do = tk.Entry(lewa_ramka, width=30, validate="key", validatecommand=(walidacja_cyfry, "%P"))
nastepstwo_do.pack(anchor='w', pady=(0, 10))

przycisk = tk.Button(lewa_ramka, text="Dodaj", command=dodanie_do_tabeli)
przycisk.pack(anchor="w", pady=(10, 0))

przycisk_usun = tk.Button(lewa_ramka, text="Usuń zaznaczony", command=usun_zaznaczony)
przycisk_usun.pack(anchor="w", pady=(5, 0))

# --- Prawa strona (tabela) ---
kolumny = ("Lp.", "Nazwa zdarzenia", "Czas trwania zdarzenia", "Nastepstwa")
tabela = ttk.Treeview(prawa_ramka, columns=kolumny, show="headings")

# Nagłówki
tabela.heading("Lp.", text="Lp.")
tabela.heading("Nazwa zdarzenia", text="Nazwa zdarzenia")
tabela.heading("Czas trwania zdarzenia", text="Czas trwania zdarzenia")
tabela.heading("Nastepstwa", text="Następstwa")

# Szerokości kolumn
tabela.column("Lp.", width=40, anchor=tk.CENTER, stretch=False)
tabela.column("Nazwa zdarzenia", width=200, anchor=tk.CENTER)
tabela.column("Czas trwania zdarzenia", width=150, anchor=tk.CENTER)
tabela.column("Nastepstwa", width=200, anchor=tk.CENTER)

tabela.pack(fill="both", expand=True)

# Pętla aplikacji
okno.mainloop()