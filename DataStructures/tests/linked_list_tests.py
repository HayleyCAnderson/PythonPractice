from nose.tools import *
from lib.linked_list import LinkedList

# add
def test_adding_node_to_linked_list():
    linked_list = LinkedList()
    linked_list.add(1)

    assert_equal(hasattr(linked_list, "Node"), True)

# count
def test_counting_nodes_in_linked_list():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)

    assert_equal(linked_list.count, 3)

# head
def test_getting_head_of_linked_list():
    linked_list = LinkedList()

    assert_equal(linked_list.head, None)
    linked_list.add(1)
    assert_equal(linked_list.head.value, 1)

# tail
def test_getting_tail_of_linked_list():
    linked_list = LinkedList()

    assert_equal(linked_list.tail, None)
    linked_list.add(1)
    assert_equal(linked_list.tail.value, 1)

# remove
def test_removing_node_from_linked_list():
    linked_list = LinkedList()
    linked_list.add(1)

    assert_equal(linked_list.remove(1), True)
    assert_equal(linked_list.count, 0)

def test_removing_first_matching_node_from_linked_list():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(1)

    assert_equal(linked_list.remove(1), True)
    assert_equal(linked_list.count, 1)

def test_removing_value_not_found_in_linked_list():
    linked_list = LinkedList()
    linked_list.add(1)

    assert_equal(linked_list.remove(2), False)
    assert_equal(linked_list.count, 1)

def test_resetting_head_and_tail_when_removing_node():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)

    assert_equal(linked_list.head.value, 1)
    assert_equal(linked_list.tail.value, 3)
    linked_list.remove(1)
    assert_equal(linked_list.head.value, 2)
    assert_equal(linked_list.tail.value, 3)
    linked_list.remove(3)
    assert_equal(linked_list.head.value, 2)
    assert_equal(linked_list.tail.value, 2)
    linked_list.remove(2)
    assert_equal(linked_list.head, None)
    assert_equal(linked_list.tail, None)

def test_resetting_pointers_when_removing_node():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)

    assert_equal(linked_list.head.next_node.value, 2)
    assert_equal(linked_list.tail.next_node, None)
    linked_list.remove(1)
    assert_equal(linked_list.head.next_node, linked_list.tail)
    assert_equal(linked_list.tail.next_node, None)
    linked_list.remove(3)
    assert_equal(linked_list.head.next_node, None)
    assert_equal(linked_list.tail.next_node, None)
    linked_list.remove(2)
    assert_equal(linked_list.count, 0)

# contains
def test_returning_whether_linked_list_contains_value():
    linked_list = LinkedList()

    assert_equal(linked_list.contains(2), False)
    linked_list.add(1)
    assert_equal(linked_list.contains(2), False)
    linked_list.add(2)
    assert_equal(linked_list.contains(2), True)
    linked_list.add(3)
    assert_equal(linked_list.contains(2), True)

# clear
def test_clearing_linked_list():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)

    assert_equal(linked_list.head.value, 1)
    assert_equal(linked_list.tail.value, 2)
    assert_equal(linked_list.count, 2)
    linked_list.clear()
    assert_equal(linked_list.head, None)
    assert_equal(linked_list.tail, None)
    assert_equal(linked_list.count, 0)
