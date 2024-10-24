# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None


def is_univalue_list(head, prev_val=None):
    if head is None:
        return True

    if prev_val is not None and head.val != prev_val:
        return False

    return is_univalue_list(head.next, prev_val=head.val)
    # current = head

    # while current is not None:
    #   if current.val != head.val:
    #     return False
    #   current = current.next
    # return True
