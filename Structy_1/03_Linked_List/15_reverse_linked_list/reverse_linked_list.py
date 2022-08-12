# My incomplete solution
def reverse_list(head):
  #   Save first next
  first_next = head.next
#   set head to null
  head.next = None
#   current_node for ease of reading
  current_node = first_next
#   start terminology
  next = current_node.next
  previous = head
  current_node.next = previous
  previous = current_node
  current_node = next
  while current_node:
    next = current_node.next

# Alvin's Solution

def iterative_reverse_list(head):
  prev = None
  current = head
  while current is not None:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev

def recursive_reverse_list(head, prev = None):
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)