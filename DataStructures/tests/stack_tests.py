from nose.tools import *
from lib.stack import Stack

# empty
def test_empty_returning_true_when_empty():
    stack = Stack()

    assert_equal(stack.empty(), True)

def test_empty_returning_false_when_not_empty():
    stack = Stack()
    stack.push(1)

    assert_equal(stack.empty(), False)

# push
def test_pushing_to_stack_adds_item_to_stack():
    stack = Stack()

    assert_equal(stack.empty(), True)
    stack.push(1)
    assert_equal(stack.empty(), False)
    assert_equal(stack.peek(), 1)

# pop
def test_popping_from_stack_returns_last_item():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert_equal(stack.pop(), 3)

def test_popping_from_stack_removes_item():
    stack = Stack()
    stack.push(1)

    assert_equal(stack.empty(), False)
    assert_equal(stack.pop(), 1)
    assert_equal(stack.empty(), True)

def test_popping_from_empty_stack_raises_custom_error_message():
    stack = Stack()

    assert_equal(stack.pop(), "Error: Stack is empty")

# peek
def test_peeking_at_stack_returns_last_item():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert_equal(stack.peek(), 3)

def test_peeking_at_stack_does_not_remove_item():
    stack = Stack()
    stack.push(1)

    assert_equal(stack.empty(), False)
    assert_equal(stack.peek(), 1)
    assert_equal(stack.empty(), False)

def test_peeking_at_empty_stack_returns_none():
    stack = Stack()

    assert_equal(stack.peek(), None)
