# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def reverse_list(head):
  previous = None
  current = head
  
  while current is not None:
    next = current.next
    current.next = previous
    previous = current
    current = next

  return previous