from form import FormularzCPM
from graph_drawer import draw_graph

import tkinter as tk

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.prev = []
        self.nxt = []
        self.early_start = 0
        self.early_finish = 0
        self.late_start = float('inf')
        self.late_finish = float('inf')
        self.reserve = 0

def cpm(tasks):
    for task in tasks.values():
        if not task.prev:
            task.early_start = 0
        else:
            task.early_start = max(tasks[p].early_finish for p in task.prev)
        task.early_finish = task.early_start + task.duration

    max_finish = max(task.early_finish for task in tasks.values())

    for task in reversed(list(tasks.values())):
        if not task.nxt:
            task.late_finish = max_finish
        else:
            task.late_finish = min(tasks[s].late_start for s in task.nxt)
        task.late_start = task.late_finish - task.duration

    critical_path = []
    for task in tasks.values():
        task.reserve = task.late_finish - task.early_finish
        if task.reserve == 0:
            critical_path.append(task)

    return critical_path, max_finish

def generuj_wykres(formularz):
    dane = formularz.pobierz_dane()
    tasks = {}

    for rekord in dane:
        lp, nazwa, czas, _ = rekord
        tasks[nazwa] = Task(nazwa, int(czas))

    for rekord in dane:
        lp, nazwa, czas, nastepstwa = rekord
        if nastepstwa.strip():
            od, do = nastepstwa.split("-")
            od = od.strip()
            do = do.strip()
            if od in tasks and do in tasks:
                tasks[od].nxt.append(do)
                tasks[do].prev.append(od)

    if "START" not in tasks:
        tasks["START"] = Task("START", 0)
        for task in tasks.values():
            if not task.prev and task.name != "START":
                tasks["START"].nxt.append(task.name)
                task.prev.append("START")

    critical_path, project_duration = cpm(tasks)
    print("Ścieżka krytyczna:", " -> ".join([task.name for task in critical_path]))
    print("Minimalny czas realizacji projektu:", project_duration)
    draw_graph(tasks, critical_path)

def main():
    root = tk.Tk()
    formularz = FormularzCPM(root)

    # Dodaj przycisk "Generuj wykres"
    przycisk_generuj = tk.Button(formularz.lewa_ramka, text="Generuj wykres", bg="green", fg="white",
                                 command=lambda: generuj_wykres(formularz))
    przycisk_generuj.pack(anchor="w", pady=(20, 0))

    root.mainloop()

if __name__ == "__main__":
    main()
