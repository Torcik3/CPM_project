from collections import defaultdict

class Task:
    def __init__(self, name, duration, prev, nxt):
        self.name = name
        self.duration = duration
        self.prev = []
        self.nxt = []
        self.early_start = 0
        self.early_finish = 0
        self.late_start = float('inf')
        self.late_finish = float('inf')
        self.rating = 0






