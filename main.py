from form import uruchom_formularz, tasks_data
from graph_drawer import draw_graph

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

# Funkcja build_successors - upewnij się, że jest przed main()
def build_successors(tasks):
    for task in tasks.values():
        task.nxt = []
    for task_name, current_task in tasks.items():
        for predecessor_name in current_task.prev:
            if predecessor_name in tasks:
                predecessor_task = tasks[predecessor_name]
                if task_name not in predecessor_task.nxt:
                    predecessor_task.nxt.append(task_name)

# Funkcja cpm - pozostała bez zmian
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

# Główna funkcja
def main():
    uruchom_formularz()  # Formularz

    # Po zamknięciu okna formularza tworzymy zadania
    tasks = {}
    tasks['START'] = Task('START', 0)

    for entry in tasks_data:
        name = entry['name']
        duration = entry['duration']
        prev = entry['prev']

        task = Task(name, duration)
        task.prev = prev if prev else ['START']
        tasks[name] = task

    build_successors(tasks)
    critical_path, project_duration = cpm(tasks)

    print("Ścieżka krytyczna:", " -> ".join([task.name for task in critical_path]))
    print("Minimalny czas realizacji projektu:", project_duration)

    draw_graph(tasks, critical_path, project_duration)

if __name__ == "__main__":
    main()
