from nose.tools import *
from problem_two.list_mixer import ListMixer

def test_combining_two_equal_lists():
    list_mixer = ListMixer()

    assert_equal(
        list_mixer.combine([1, 2, 3], ["a", "b", "c"]),
        [1, "a", 2, "b", 3, "c"]
    )

def test_combining_two_lists_with_first_longer():
    list_mixer = ListMixer()

    assert_equal(
        list_mixer.combine([1, 2, 3, 4, 5], ["a", "b", "c"]),
        [1, "a", 2, "b", 3, "c", 4, 5]
    )

def test_combining_two_lists_with_second_longer():
    list_mixer = ListMixer()

    assert_equal(
        list_mixer.combine([1, 2, 3], ["a", "b", "c", "d", "e"]),
        [1, "a", 2, "b", 3, "c", "d", "e"]
    )
