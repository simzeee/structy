# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None


def linked_list_values(head):
    current = head
    vals = []
    while current is not None:
        vals.append(current.val)
        current = current.next

    return vals


def linked_list_values_recursive(head):
    values = []
    fill_values(head, values)
    return values


def fill_values(head, values):
    if head is None:
        return
    values.append(head.val)
    fill_values(head.next, values)
