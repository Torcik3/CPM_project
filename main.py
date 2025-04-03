from collections import defaultdict

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
    # early start and finish
    for task in tasks.values():
        if not task.prev:
            task.early_start = 0
        else:
            task.early_start = max(tasks[p].early_finish for p in task.prev)
        task.early_finish = task.early_start + task.duration

    # max completion time
    max_finish = max(task.early_finish for task in tasks.values())

    # late start and finish
    for task in reversed(list(tasks.values())):
        if not task.nxt:
            task.late_finish = max_finish
        else:
            task.late_finish = min(tasks[s].late_start for s in task.nxt)
        task.late_start = task.late_finish - task.duration

    # reserve and critical path
    critical_path = []
    for task in tasks.values():
        task.reserve = task.late_finish - task.early_finish
        if task.reserve == 0:
            critical_path.append(task)

    return critical_path, max_finish


def main():
    tasks = {
        'A': Task('A', 2),
        'B': Task('B', 5),
        'C': Task('C', 1),
        'D': Task('D', 6),
        'E': Task('E', 4),
        'F': Task('F', 2)
    }

    tasks['A'].nxt = ['C']
    tasks['B'].nxt = ['C', 'D']
    tasks['C'].nxt = ['E']
    tasks['D'].nxt = ['E', 'F']

    tasks['C'].prev = ['A', 'B']
    tasks['D'].prev = ['B']
    tasks['E'].prev = ['C', 'D']
    tasks['F'].prev = ['D']

    critical_path, project_duration = cpm(tasks)
    print("Ścieżka krytyczna:", " -> ".join([task.name for task in critical_path]))
    print("Minimalny czas realizacji projektu:", project_duration)



main()



