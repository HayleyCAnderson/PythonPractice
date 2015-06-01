from nose.tools import *
from lib.queue import Queue

# empty
def test_empty_returning_true_when_empty():
    queue = Queue()

    assert_equal(queue.empty(), True)

def test_empty_returning_false_when_not_empty():
    queue = Queue()
    queue.enqueue(1)

    assert_equal(queue.empty(), False)

# enqueue
def test_enqueuing_to_queue_adds_item_to_queue():
    queue = Queue()

    assert_equal(queue.empty(), True)
    queue.enqueue(1)
    assert_equal(queue.empty(), False)
    assert_equal(queue.dequeue(), 1)

# dequeue
def test_dequeuing_from_queue_returns_first_item():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert_equal(queue.dequeue(), 1)

def test_dequeuing_from_queue_removes_item():
    queue = Queue()
    queue.enqueue(1)

    assert_equal(queue.empty(), False)
    assert_equal(queue.dequeue(), 1)
    assert_equal(queue.empty(), True)

def test_dequeuing_from_empty_queue_raises_custom_error_message():
    queue = Queue()

    assert_equal(queue.dequeue(), "Error: Queue is empty")
