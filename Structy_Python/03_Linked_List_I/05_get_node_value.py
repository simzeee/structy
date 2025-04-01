# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None


def get_node_value(head, index):
    current = head
    tracker = 0
    while current is not None:
        if index == tracker:
            return current.val
        current = current.next
        tracker += 1


def get_node_value_recursive(head, index):
    if head is None:
        return None
    if index == 0:
        return head.val
    return get_node_value(head.next, index - 1)
