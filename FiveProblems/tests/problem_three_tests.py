from nose.tools import *
from problem_three.fibonacci import Fibonacci

def test_calculating_list_of_fibonacci_numbers():
    sequence = Fibonacci(10)

    assert_equal(sequence.return_numbers(), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
