from core.treasurehunter import (hunt_treasure,
                                 TreasureHunter,
                                 to_index, to_val)
import pytest


example_data = [[55, 14, 25, 52, 21],
                [44, 31, 11, 53, 43],
                [24, 13, 45, 12, 34],
                [42, 22, 43, 32, 41],
                [51, 23, 33, 54, 15]]


example_expectation = [11, 55, 15, 21, 44, 32, 13, 25, 43]


task_data = [[34, 21, 32, 41, 25],
             [14, 42, 43, 14, 31],
             [54, 45, 52, 42, 23],
             [33, 15, 51, 31, 35],
             [21, 52, 33, 13, 23]]


task_expectattion = [11, 34, 42, 15, 25, 31, 54, 13, 32,
                     45, 35, 23, 43, 51, 21, 14, 41, 33, 52]


def test_to_index():
    with pytest.raises(ValueError):
        to_index(99)


def test_to_val():
    with pytest.raises(ValueError):
        to_val(6, 7)


def test_hunt_treasure_with_example_data():
    assert hunt_treasure(example_data) == example_expectation


def test_hunt_treasure_with_task_data():
    assert hunt_treasure(task_data) == task_expectattion


def test_treasure_hunter_with_example_data():
    hunter = TreasureHunter(example_data)
    assert [item for item in hunter] == example_expectation
    # let's ensure that iterator will reset position
    assert [item for item in hunter] == example_expectation


def test_treasure_hunter_with_task_data():
    hunter = TreasureHunter(task_data)
    assert [item for item in hunter] == task_expectattion
