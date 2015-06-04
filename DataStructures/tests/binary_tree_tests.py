from nose.tools import *
from lib.binary_tree import BinaryTree

# add
def test_adding_node_to_empty_binary_tree():
    binary_tree = BinaryTree()
    binary_tree.add(1)

    assert_equal(hasattr(binary_tree, "Node"), True)
    assert_equal(binary_tree.count, 1)
    assert_equal(binary_tree.head.value, 1)

def test_adding_nodes_to_left_of_binary_tree():
    binary_tree = BinaryTree()
    binary_tree.add(8)
    binary_tree.add(5)
    binary_tree.add(2)

    assert_equal(binary_tree.count, 3)
    assert_equal(binary_tree.head.value, 8)
    assert_equal(binary_tree.head.left.value, 5)
    assert_equal(binary_tree.head.left.left.value, 2)

def test_adding_nodes_to_right_of_binary_tree():
    binary_tree = BinaryTree()
    binary_tree.add(8)
    binary_tree.add(10)
    binary_tree.add(12)

    assert_equal(binary_tree.count, 3)
    assert_equal(binary_tree.head.value, 8)
    assert_equal(binary_tree.head.right.value, 10)
    assert_equal(binary_tree.head.right.right.value, 12)

def test_adding_equal_nodes_to_binary_tree():
    binary_tree = BinaryTree()
    binary_tree.add(1)
    binary_tree.add(1)
    binary_tree.add(1)

    assert_equal(binary_tree.count, 3)
    assert_equal(binary_tree.head.value, 1)
    assert_equal(binary_tree.head.right.value, 1)
    assert_equal(binary_tree.head.right.right.value, 1)

def test_adding_nodes_to_full_binary_tree():
    binary_tree = BinaryTree()
    binary_tree.add(8)
    binary_tree.add(4)
    binary_tree.add(10)
    binary_tree.add(2)
    binary_tree.add(6)
    binary_tree.add(3)
    binary_tree.add(7)

    assert_equal(binary_tree.count, 7)
    assert_equal(binary_tree.head.value, 8)
    assert_equal(binary_tree.head.left.value, 4)
    assert_equal(binary_tree.head.right.value, 10)
    assert_equal(binary_tree.head.left.left.value, 2)
    assert_equal(binary_tree.head.left.right.value, 6)
    assert_equal(binary_tree.head.left.left.right.value, 3)
    assert_equal(binary_tree.head.left.right.right.value, 7)

# remove
def test_removing_node_from_empty_binary_tree():
    binary_tree = BinaryTree()

    assert_equal(binary_tree.remove(1), False)
    assert_equal(binary_tree.count, 0)

def test_removing_node_from_binary_tree_without_match():
    binary_tree = BinaryTree()
    binary_tree.add(8)
    binary_tree.add(5)
    binary_tree.add(2)

    assert_equal(binary_tree.remove(1), False)
    assert_equal(binary_tree.count, 3)

def test_removing_node_without_right_from_binary_tree():
    binary_tree = BinaryTree()
    binary_tree.add(8)
    binary_tree.add(5)
    binary_tree.add(10)
    binary_tree.add(2)

    assert_equal(binary_tree.remove(5), True)
    assert_equal(binary_tree.count, 3)
    assert_equal(binary_tree.head.value, 8)
    assert_equal(binary_tree.head.left.value, 2)
    assert_equal(binary_tree.head.right.value, 10)

def test_removing_head_node_without_right_from_binary_tree():
    binary_tree = BinaryTree()
    binary_tree.add(8)
    binary_tree.add(5)
    binary_tree.add(2)

    assert_equal(binary_tree.remove(8), True)
    assert_equal(binary_tree.count, 2)
    assert_equal(binary_tree.head.value, 5)
    assert_equal(binary_tree.head.left.value, 2)

def test_removing_node_with_right_without_left_from_binary_tree():
    binary_tree = BinaryTree()
    binary_tree.add(8)
    binary_tree.add(5)
    binary_tree.add(10)
    binary_tree.add(2)
    binary_tree.add(6)
    binary_tree.add(7)

    assert_equal(binary_tree.remove(5), True)
    assert_equal(binary_tree.count, 5)
    assert_equal(binary_tree.head.value, 8)
    assert_equal(binary_tree.head.left.value, 6)
    assert_equal(binary_tree.head.right.value, 10)
    assert_equal(binary_tree.head.left.left.value, 2)
    assert_equal(binary_tree.head.left.right.value, 7)

def test_removing_head_node_with_right_without_left_from_binary_tree():
    binary_tree = BinaryTree()
    binary_tree.add(8)
    binary_tree.add(5)
    binary_tree.add(10)
    binary_tree.add(2)

    assert_equal(binary_tree.remove(8), True)
    assert_equal(binary_tree.count, 3)
    assert_equal(binary_tree.head.value, 10)
    assert_equal(binary_tree.head.left.value, 5)
    assert_equal(binary_tree.head.left.left.value, 2)

def test_removing_node_with_right_with_left_from_binary_tree():
    binary_tree = BinaryTree()
    binary_tree.add(8)
    binary_tree.add(5)
    binary_tree.add(10)
    binary_tree.add(2)
    binary_tree.add(7)
    binary_tree.add(6)

    assert_equal(binary_tree.remove(5), True)
    assert_equal(binary_tree.count, 5)
    assert_equal(binary_tree.head.value, 8)
    assert_equal(binary_tree.head.left.value, 6)
    assert_equal(binary_tree.head.right.value, 10)
    assert_equal(binary_tree.head.left.left.value, 2)
    assert_equal(binary_tree.head.left.right.value, 7)

def test_removing_head_node_with_right_with_left_from_binary_tree():
    binary_tree = BinaryTree()
    binary_tree.add(8)
    binary_tree.add(5)
    binary_tree.add(10)
    binary_tree.add(9)

    assert_equal(binary_tree.remove(8), True)
    assert_equal(binary_tree.count, 3)
    assert_equal(binary_tree.head.value, 9)
    assert_equal(binary_tree.head.left.value, 5)
    assert_equal(binary_tree.head.right.value, 10)

# contains
def test_finding_value_in_binary_tree_with_value():
    binary_tree = BinaryTree()
    binary_tree.add(8)
    binary_tree.add(5)
    binary_tree.add(10)
    binary_tree.add(2)
    binary_tree.add(7)
    binary_tree.add(6)

    assert_equal(binary_tree.contains(2), True)
    assert_equal(binary_tree.contains(5), True)
    assert_equal(binary_tree.contains(6), True)
    assert_equal(binary_tree.count, 6)

def test_finding_value_in_binary_tree_without_value():
    binary_tree = BinaryTree()
    binary_tree.add(8)
    binary_tree.add(5)
    binary_tree.add(10)
    binary_tree.add(2)
    binary_tree.add(7)
    binary_tree.add(6)

    assert_equal(binary_tree.contains(1), False)
    assert_equal(binary_tree.contains(3), False)
    assert_equal(binary_tree.contains(4), False)
    assert_equal(binary_tree.count, 6)

def test_finding_value_in_empty_binary_tree():
    binary_tree = BinaryTree()

    assert_equal(binary_tree.contains(1), False)
    assert_equal(binary_tree.count, 0)

#clear
def test_clearing_binary_tree():
    binary_tree = BinaryTree()
    binary_tree.add(8)
    binary_tree.add(5)
    binary_tree.add(2)
    binary_tree.clear()

    assert_equal(binary_tree.count, 0)
    assert_equal(binary_tree.head, None)
