from queue import PriorityQueue


class MaxHeapPriorityQueue:
    def __init__(self):
        self.queue = PriorityQueue()

    def push(self, priority, item):
        self.queue.put((-priority, item))

    def pop(self):
        (_, item) = self.queue.get()
        return item

    def is_empty(self):
        return self.queue.empty()
    