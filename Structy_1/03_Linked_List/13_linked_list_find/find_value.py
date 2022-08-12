class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    
def linked_list_find(head, target):
  if head is None:
    return False
  if head.val == target:
    return True
  return linked_list_find(head.next, target)

# def linked_list_find(head, target):
#   current_node = head
#   while current_node is not None:
#     if current_node.val == target:
#       return True
#     current_node = current_node.next
#   return False

# Both have O(n), but iterative uses constant space and recursive uses linear because of callstack creations

# Alvin's Solutions

def linked_list_find(head, target):
  current = head
  while current is not None:
    if current.val == target:
      return True
    current = current.next
  return False

def linked_list_find(head, target):
  if head is None:
    return False
  if head.val == target:
    return True
  return linked_list_find(head.next, target)