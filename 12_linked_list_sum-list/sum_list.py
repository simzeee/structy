class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


# My Iterative Solution

def sum_list(head):
  current_node = head
  sum = 0
  while current_node:
    sum += current_node.val
    current_node = current_node.next
  return sum

# My Recursive Solution

def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)