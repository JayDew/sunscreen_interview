from main import find_center, hungry_rabbit_util


def test_find_center_odd_odd():
    garden = [
        [5, 7, 8, 6, 3],
        [0, 0, 420, 0, 4],
        [4, 6, 3, 4, 9]
    ]

    assert (1, 2) == find_center(garden)


def test_find_center_odd_even():
    garden = [
        [5, 7, 8, 6],
        [0, 420, 7, 0],
        [4, 6, 3, 4]
    ]

    assert (1, 1) == find_center(garden)


def test_find_center_even_odd():
    garden = [
        [5, 420, 8],
        [0, 10, 7]
    ]

    assert (0, 1) == find_center(garden)


def test_find_center_even_even():
    garden = [
        [5, 420],
        [0, 10]
    ]

    assert (0, 1) == find_center(garden)


def test_hungry_rabbit_util():
    garden = [
        [5, 420],
        [0, 10]
    ]
    assert 430 == hungry_rabbit_util(garden, 0, 1), "Should consume 420 + 10"


def test_hungry_rabbit_util_consume_all_board():
    garden = [
        [5, 420],
        [0, 10]
    ]
    assert 435 == hungry_rabbit_util(garden, 1, 0), "Should consume 10 + 420 + 5"


def test_hungry_rabbit_one_element():
    garden = [[5]]
    assert 5 == hungry_rabbit_util(garden, 0, 0)
