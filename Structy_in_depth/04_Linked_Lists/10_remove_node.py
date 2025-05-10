class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_node(head, target_val):

    if head.val == target_val:
        new_head = head.next
        head.next = None
        return new_head

    current = head
    previous = None
    removed = False

    while current is not None:

        if current.val == target_val and removed is False:
            previous.next = current.next
            new_next = current.next
            current.next = None
            current = new_next
            removed = True

        else:
            previous = current
            current = current.next

    return head
