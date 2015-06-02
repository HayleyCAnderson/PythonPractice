from nose.tools import *
from lib.doubly_linked_list import DoublyLinkedList

# add_last
def test_adding_node_to_end_of_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.add_last(1)
    doubly_linked_list.add_last(2)

    assert_equal(hasattr(doubly_linked_list, "Node"), True)
    assert_equal(doubly_linked_list.count, 2)
    assert_equal(doubly_linked_list.tail.value, 2)

# add_first
def test_adding_node_to_beginning_of_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.add_first(1)
    doubly_linked_list.add_first(2)

    assert_equal(hasattr(doubly_linked_list, "Node"), True)
    assert_equal(doubly_linked_list.count, 2)
    assert_equal(doubly_linked_list.head.value, 2)

# remove_last
def test_removing_node_from_end_of_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.add_last(1)
    doubly_linked_list.add_last(2)
    doubly_linked_list.add_last(3)

    assert_equal(doubly_linked_list.remove_last(), True)
    assert_equal(doubly_linked_list.count, 2)
    assert_equal(doubly_linked_list.tail.value, 2)

def test_removing_node_from_end_of_one_node_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.add_last(1)

    assert_equal(doubly_linked_list.remove_last(), True)
    assert_equal(doubly_linked_list.count, 0)
    assert_equal(doubly_linked_list.tail, None)

def test_removing_node_from_end_of_empty_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()

    assert_equal(doubly_linked_list.remove_last(), False)
    assert_equal(doubly_linked_list.count, 0)
    assert_equal(doubly_linked_list.tail, None)

# remove_first
def test_removing_node_from_beginning_of_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.add_first(1)
    doubly_linked_list.add_first(2)
    doubly_linked_list.add_first(3)

    assert_equal(doubly_linked_list.remove_first(), True)
    assert_equal(doubly_linked_list.count, 2)
    assert_equal(doubly_linked_list.head.value, 2)

def test_removing_node_from_beginning_of_one_node_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.add_first(1)

    assert_equal(doubly_linked_list.remove_first(), True)
    assert_equal(doubly_linked_list.count, 0)
    assert_equal(doubly_linked_list.head, None)

def test_removing_node_from_beginning_of_empty_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()

    assert_equal(doubly_linked_list.remove_first(), False)
    assert_equal(doubly_linked_list.count, 0)
    assert_equal(doubly_linked_list.head, None)

# remove
def test_removing_matching_node_from_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.add_last(1)
    doubly_linked_list.add_last(2)
    doubly_linked_list.add_last(3)

    assert_equal(doubly_linked_list.remove(2), True)
    assert_equal(doubly_linked_list.count, 2)
    assert_equal(doubly_linked_list.head.value, 1)
    assert_equal(doubly_linked_list.tail.value, 3)

def test_removing_matching_node_from_head_of_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.add_last(1)
    doubly_linked_list.add_last(2)
    doubly_linked_list.add_last(3)

    assert_equal(doubly_linked_list.remove(1), True)
    assert_equal(doubly_linked_list.count, 2)
    assert_equal(doubly_linked_list.head.value, 2)
    assert_equal(doubly_linked_list.tail.value, 3)

def test_removing_matching_node_from_tail_of_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.add_last(1)
    doubly_linked_list.add_last(2)
    doubly_linked_list.add_last(3)

    assert_equal(doubly_linked_list.remove(3), True)
    assert_equal(doubly_linked_list.count, 2)
    assert_equal(doubly_linked_list.head.value, 1)
    assert_equal(doubly_linked_list.tail.value, 2)

def test_removing_without_matching_node_from_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.add_last(1)
    doubly_linked_list.add_last(2)
    doubly_linked_list.add_last(3)

    assert_equal(doubly_linked_list.remove(4), False)
    assert_equal(doubly_linked_list.count, 3)
    assert_equal(doubly_linked_list.head.value, 1)
    assert_equal(doubly_linked_list.tail.value, 3)

# clear
def test_clearing_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.add_last(1)
    doubly_linked_list.add_last(2)
    doubly_linked_list.add_last(3)

    assert_equal(doubly_linked_list.clear(), True)
    assert_equal(doubly_linked_list.count, 0)
