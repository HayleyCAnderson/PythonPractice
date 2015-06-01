class Queue(object):
    # O(1)
    def __init__(self):
        self.queue = []

    # O(1)
    def empty(self):
        if self.queue:
            return False
        else:
            return True

    # O(1)
    def enqueue(self, item):
        self.queue.append(item)

    # O(1)
    def dequeue(self):
        try:
            return self.queue.pop(0)
        except IndexError:
            return "Error: Queue is empty"
