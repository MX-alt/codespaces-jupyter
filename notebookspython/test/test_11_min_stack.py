import pytest

from helpers import load_py


mod = load_py("11-min_stack.py", "min_stack")


def test_min_stack_tracks_minimum_through_push_and_pop():
    stack = mod.MinStack()

    stack.push(3)
    stack.push(5)
    stack.push(1)
    stack.push(2)

    assert stack.min() == 1
    assert stack.top() == 2

    stack.pop()
    stack.pop()

    assert stack.min() == 3
    assert stack.top() == 5


def test_min_stack_handles_duplicate_minimums():
    stack = mod.MinStack()

    stack.push(3)
    stack.push(3)
    stack.pop()

    assert stack.min() == 3


def test_min_stack_empty_operations_raise_index_error():
    stack = mod.MinStack()

    with pytest.raises(IndexError):
        stack.pop()
    with pytest.raises(IndexError):
        stack.top()
    with pytest.raises(IndexError):
        stack.min()
