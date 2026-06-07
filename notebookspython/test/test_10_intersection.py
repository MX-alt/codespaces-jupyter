import pytest

from helpers import load_py


mod = load_py("10-intersection.py", "intersection")


@pytest.mark.parametrize("solver_cls", [mod.Solution, mod.SolutionSet, mod.SolutionTwoPointer])
def test_get_intersection_node(solver_cls):
    intersection_node = mod.build_shared_tail([8, 4, 5])
    head_a = mod.build_prefix([4, 1], intersection_node)
    head_b = mod.build_prefix([5, 6, 1], intersection_node)

    result = solver_cls().getIntersectionNode(head_a, head_b)

    assert result is intersection_node
    assert result.val == 8


@pytest.mark.parametrize("solver_cls", [mod.Solution, mod.SolutionSet, mod.SolutionTwoPointer])
def test_get_intersection_node_with_no_intersection(solver_cls):
    head_a = mod.build_shared_tail([1, 2, 3])
    head_b = mod.build_shared_tail([4, 5, 6])

    assert solver_cls().getIntersectionNode(head_a, head_b) is None


@pytest.mark.parametrize("solver_cls", [mod.Solution, mod.SolutionSet, mod.SolutionTwoPointer])
def test_get_intersection_node_empty_inputs(solver_cls):
    single = mod.build_shared_tail([1])

    assert solver_cls().getIntersectionNode(None, None) is None
    assert solver_cls().getIntersectionNode(None, single) is None
    assert solver_cls().getIntersectionNode(single, None) is None
