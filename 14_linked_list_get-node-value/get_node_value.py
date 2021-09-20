# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def get_node_value(head, index):
#   i = 0
#   current = head
#   while current is not None:
#     if i == index:
#       return current.val
#     else:
#       i += 1
#       current = current.next
#   return None


def get_node_value(head, index):
  
  if head is None:
    return None
  if 0 == index:
    return head.val
  return get_node_value(head.next, index - 1)

  # Iterative => T: O(n) S: O(1)
  # Recursive => T: O(n) S: (On)