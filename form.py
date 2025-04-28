import tkinter as tk
from tkinter import ttk

tasks_data = []  # Tutaj będą dane do zapisania

def dodaj_do_listy():
    nazwa = nazwa_zdarzenia.get()
    czas = t_zdarzenia.get()
    poprzednik = poprzednik_entry.get()

    if not nazwa or not czas:
        return  # brak wymaganych danych

    task = {
        "name": nazwa,
        "duration": int(czas),
        "prev": poprzednik.split(",") if poprzednik else []
    }
    tasks_data.append(task)

    # Dodaj do tabeli widocznej
    tabela.insert("", "end", values=(nazwa, czas, poprzednik))

    # Wyczyść pola
    nazwa_zdarzenia.delete(0, tk.END)
    t_zdarzenia.delete(0, tk.END)
    poprzednik_entry.delete(0, tk.END)

def uruchom_formularz():
    global nazwa_zdarzenia, t_zdarzenia, poprzednik_entry, tabela

    okno = tk.Tk()
    okno.title("Formularz CPM")
    okno.geometry("700x500")

    frame = tk.Frame(okno)
    frame.pack(padx=10, pady=10)

    tk.Label(frame, text="Nazwa zadania:").grid(row=0, column=0, sticky="w")
    nazwa_zdarzenia = tk.Entry(frame, width=30)
    nazwa_zdarzenia.grid(row=0, column=1)

    tk.Label(frame, text="Czas trwania:").grid(row=1, column=0, sticky="w")
    t_zdarzenia = tk.Entry(frame, width=30)
    t_zdarzenia.grid(row=1, column=1)

    tk.Label(frame, text="Poprzednicy (oddziel ',' jeśli kilka):").grid(row=2, column=0, sticky="w")
    poprzednik_entry = tk.Entry(frame, width=30)
    poprzednik_entry.grid(row=2, column=1)

    tk.Button(frame, text="Dodaj zadanie", command=dodaj_do_listy).grid(row=3, column=1, pady=10)

    tabela = ttk.Treeview(okno, columns=("nazwa", "czas", "poprzednicy"), show="headings")
    tabela.heading("nazwa", text="Nazwa zadania")
    tabela.heading("czas", text="Czas trwania")
    tabela.heading("poprzednicy", text="Poprzednicy")
    tabela.pack(fill="both", expand=True)

    tk.Button(okno, text="Zapisz i Zamknij", command=okno.destroy).pack(pady=10)

    okno.mainloop()
