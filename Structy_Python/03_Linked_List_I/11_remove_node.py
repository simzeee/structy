# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None


def remove_node(head, target_val):

    if head.val == target_val:
        new_head = head.next
        head.next = None
        return new_head

    current = head
    previous = None

    while current is not None:

        if current.val == target_val:
            new_next = current.next
            previous.next = new_next
            current.next = None
            return head
        else:
            previous = current
            current = current.next
