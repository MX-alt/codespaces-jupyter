from helpers import linked_values, load_py


mod = load_py("05-remove_duplicate_nodes.py", "remove_duplicate_nodes")


def test_remove_duplicate_nodes_keeps_first_occurrences():
    head = mod.create_linked_list([1, 2, 3, 3, 2, 1])

    result = mod.Solution().removeDuplicateNodes(head)

    assert linked_values(result) == [1, 2, 3]


def test_remove_duplicate_nodes_empty_list():
    assert mod.Solution().removeDuplicateNodes(None) is None


def test_remove_duplicate_nodes_without_duplicates():
    head = mod.create_linked_list([1, 2, 3])

    result = mod.Solution().removeDuplicateNodes(head)

    assert linked_values(result) == [1, 2, 3]
