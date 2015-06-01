class LinkedList(object):
    # O(1)
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # O(1)
    def add(self, value):
        new_node = self.Node(value)

        if self.tail != None:
            self.tail.next_node = new_node

        if self.head == None:
            self.head = new_node

        self.tail = new_node
        self.count += 1

    # O(n)
    def remove(self, value):
        return self.find_node(None, self.head, value)

    # O(n)
    def contains(self, value):
        return self.find_value(None, self.head, value)

    # O(1)
    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0

    # Helper methods
    def find_node(self, previous_node, current_node, value):
        if current_node == None:
            return False
        elif current_node.value == value:
            self.update_pointers(previous_node, current_node)
            self.count -= 1
            return True
        else:
            return self.find_node(current_node, current_node.next_node, value)

    def update_pointers(self, previous_node, current_node):
        if previous_node == None:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node

        if current_node == self.tail:
            self.tail = previous_node

    def find_value(self, previous_node, current_node, value):
        if current_node == None:
            return False
        elif current_node.value == value:
            return True
        else:
            return self.find_value(current_node, current_node.next_node, value)

    class Node(object):
        # O(1)
        def __init__(self, value):
            self.value = value
            self.next_node = None
