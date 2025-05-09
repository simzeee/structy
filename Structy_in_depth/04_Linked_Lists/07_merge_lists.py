class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_lists(head_1, head_2):
    current_1 = head_1
    current_2 = head_2
    dummy_node = Node(None)
    tail = dummy_node

    while current_1 is not None and current_2 is not None:
        if current_1.val < current_2.val:
            tail.next = current_1
            current_1 = current_1.next

        else:
            tail.next = current_2
            current_2 = current_2.next
        tail = tail.next

    if current_1 is not None:
        tail.next = current_1
    if current_2 is not None:
        tail.next = current_2

    return dummy_node.next
