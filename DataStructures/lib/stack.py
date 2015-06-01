class Stack(object):
    # O(1)
    def __init__(self):
        self.stack = []

    # O(1)
    def empty(self):
        if self.stack:
            return False
        else:
            return True

    # O(1)
    def push(self, item):
        self.stack.append(item)

    # O(1)
    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            return "Error: Stack is empty"

    # O(1)
    def peek(self):
        try:
            return self.stack[-1]
        except IndexError:
            return None
