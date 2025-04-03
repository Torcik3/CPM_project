from collections import defaultdict

class Task:
    def __init__(self, name, duration, prev, next, early_start, early_finish, rating):
        self.name = name
        self.duration = duration
        self.prev = prev
        self.next = next
        self.early_start = early_start
        self.early_finish = early_finish
        self.rating = rating

