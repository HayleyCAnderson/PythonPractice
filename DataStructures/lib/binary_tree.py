class BinaryTree(object):
    # O(1)
    def __init__(self):
        self.head = None
        self.count = 0

    # O(log n)
    def add(self, value):
        if self.count == 0:
            self.head = self.Node(value)
        else:
            self.place_node(self.head, value)

        self.count += 1

    # O(log n)
    def remove(self, value):
        if self.count == 0:
            return False
        else:
            return self.find_node(self.head, None, value, True)

    # O(log n)
    def contains(self, value):
        if self.count == 0:
            return False
        else:
            return self.find_node(self.head, None, value, False)

    # O(1)
    def clear(self):
        self.head = None
        self.count = 0

    # Helper methods
    def place_node(self, current_node, value):
        if current_node.value > value:
            if current_node.left == None:
                current_node.left = self.Node(value)
            else:
                self.place_node(current_node.left, value)
        else:
            if current_node.right == None:
                current_node.right = self.Node(value)
            else:
                self.place_node(current_node.right, value)

    def find_node(self, current_node, previous_node, value, remove):
        if current_node.value == value:
            if remove == True:
                self.remove_node(current_node, previous_node)
                self.count -= 1

            return True
        elif current_node.value > value:
            if current_node.left == None:
                return False
            else:
                return self.find_node(current_node.left, current_node, value, remove)
        else:
            if current_node.right == None:
                return False
            else:
                return self.find_node(current_node.right, current_node, value, remove)

    def remove_node(self, current_node, previous_node):
        if current_node.right == None:
            self.remove_node_without_right(current_node, previous_node)
        elif current_node.right.left == None:
            self.remove_node_with_right_without_left(current_node, previous_node)
        else:
            self.remove_node_with_right_with_left(current_node, previous_node)

    def remove_node_without_right(self, current_node, previous_node):
        if previous_node == None:
            self.head = current_node.left
        else:
            if current_node == previous_node.left:
                previous_node.left = current_node.left
            else:
                previous_node.right = current_node.left

    def remove_node_with_right_without_left(self, current_node, previous_node):
        if previous_node == None:
            self.head = current_node.right
            self.head.left = current_node.left
        else:
            if current_node == previous_node.left:
                previous_node.left = current_node.right
                previous_node.left.left = current_node.left
            else:
                previous_node.right = current_node.right
                previous_node.right.left = current_node.left

    def remove_node_with_right_with_left(self, current_node, previous_node):
        leftmost_node = current_node.right.left
        node_before_leftmost = current_node.right

        if leftmost_node.left != None:
            node_before_leftmost = leftmost_node
            leftmost_node = leftmost_node.left

        node_before_leftmost.left = leftmost_node.right
        leftmost_node.left = current_node.left
        leftmost_node.right = current_node.right

        if previous_node == None:
            self.head = leftmost_node
        else:
            if current_node == previous_node.left:
                previous_node.left = leftmost_node
            else:
                previous_node.right = leftmost_node

    class Node(object):
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
