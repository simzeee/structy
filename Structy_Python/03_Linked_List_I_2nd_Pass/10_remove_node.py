# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None


def remove_node(head, target_val):
    current = head
    prev = None

    if head.val == target_val:
        result = head.next
        head.next = None
        return result

    while current is not None:
        if current.val == target_val:
            prev.next = current.next
            current.next = None
            return head
        else:
            prev = current
            current = current.next
    return head
