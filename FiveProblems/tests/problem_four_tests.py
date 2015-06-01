from nose.tools import *
from problem_four.number_maker import NumberMaker

def test_forming_biggest_number():
    number_maker = NumberMaker()

    assert_equal(number_maker.biggest_number([50, 2, 1, 9]), 95021)
    assert_equal(number_maker.biggest_number([11, 23, 3, 40]), 4032311)

def test_forming_biggest_number_from_same_numbers():
    number_maker = NumberMaker()

    assert_equal(number_maker.biggest_number([1, 1, 1, 1]), 1111)
    assert_equal(number_maker.biggest_number([9, 9, 9, 9]), 9999)

def test_forming_biggest_number_from_same_digits():
    number_maker = NumberMaker()

    assert_equal(number_maker.biggest_number([100, 1, 1000, 10]), 1101001000)
    assert_equal(number_maker.biggest_number([110, 1, 1010, 11]), 1111101010)

def test_forming_biggest_number_from_mixed_duplicates():
    number_maker = NumberMaker()

    assert_equal(number_maker.biggest_number([110, 43, 10, 40]), 434011010)
    assert_equal(number_maker.biggest_number([4, 10, 400, 43, 5]), 544340010)
