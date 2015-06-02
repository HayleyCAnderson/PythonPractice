class DoublyLinkedList(object):
    # O(1)
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # O(1)
    def add_last(self, value):
        new_node = self.Node(value)

        if self.count == 0:
            self.head = new_node
        else:
            self.tail.next_node = new_node

        new_node.previous_node = self.tail
        self.tail = new_node
        self.count += 1

    # O(1)
    def add_first(self, value):
        new_node = self.Node(value)

        if self.count == 0:
            self.tail = new_node
        else:
            self.head.previous_node = new_node

        new_node.next_node = self.head
        self.head = new_node
        self.count += 1

    # O(1)
    def remove_last(self):
        if self.count == 0:
            return False
        elif self.count == 1:
            return self.clear()
        else:
            self.tail = self.tail.previous_node
            self.tail.next_node = None
            self.count -= 1
            return True

    # O(1)
    def remove_first(self):
        if self.count == 0:
            return False
        elif self.count == 1:
            return self.clear()
        else:
            self.head = self.head.next_node
            self.head.previous_node = None
            self.count -= 1
            return True

    # O(n)
    def remove(self, value):
        return self.find_node(self.head, value)

    # O(1)
    def clear(self):
        self.tail = None
        self.head = None
        self.count = 0
        return True

    #Helper methods
    def find_node(self, current_node, value):
        if current_node == None:
            return False
        elif current_node.value == value:
            self.update_next(current_node)
            self.update_previous(current_node)
            self.count -= 1
            return True
        else:
            return self.find_node(current_node.next_node, value)

    def update_next(self, current_node):
        if current_node == self.head:
            self.head = current_node.next_node
            self.head.previous_node = None
        else:
            current_node.previous_node.next_node = current_node.next_node

    def update_previous(self, current_node):
        if current_node == self.tail:
            self.tail = current_node.previous_node
            self.tail.next_node = None
        else:
            current_node.next_node.previous_node = current_node.previous_node

    class Node(object):
        def __init__(self, value):
            self.value = value
            self.previous_node = None
            self.next_node = None
