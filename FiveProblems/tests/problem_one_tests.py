from nose.tools import *
from problem_one.list_summer import ListSummer

def test_summing_using_for_loop():
    list_summer = ListSummer()

    assert_equal(list_summer.sum_with_for([1]), 1)
    assert_equal(list_summer.sum_with_for([1, 2, 3]), 6)
    assert_equal(list_summer.sum_with_for([9, 7, 5, 3, 1]), 25)

def test_summing_using_while_loop():
    list_summer = ListSummer()

    assert_equal(list_summer.sum_with_while([1]), 1)
    assert_equal(list_summer.sum_with_while([1, 2, 3]), 6)
    assert_equal(list_summer.sum_with_while([9, 7, 5, 3, 1]), 25)

def test_summing_using_recursion():
    list_summer = ListSummer()

    assert_equal(list_summer.sum_with_recursion([1]), 1)
    assert_equal(list_summer.sum_with_recursion([1, 2, 3]), 6)
    assert_equal(list_summer.sum_with_recursion([9, 7, 5, 3, 1]), 25)
