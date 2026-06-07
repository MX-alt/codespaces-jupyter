from helpers import linked_values, load_py


mod = load_py("07-delete_node.py", "delete_node")


def test_delete_middle_node():
    head = mod.ListNode(4)
    node_to_delete = mod.ListNode(5)
    head.next = node_to_delete
    node_to_delete.next = mod.ListNode(1)
    node_to_delete.next.next = mod.ListNode(9)

    mod.Solution().deleteNode(node_to_delete)

    assert linked_values(head) == [4, 1, 9]


def test_delete_second_to_last_node():
    head = mod.ListNode(1)
    node_to_delete = mod.ListNode(2)
    head.next = node_to_delete
    node_to_delete.next = mod.ListNode(3)

    mod.Solution().deleteNode(node_to_delete)

    assert linked_values(head) == [1, 3]
