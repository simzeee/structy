class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
# My Solution
def linked_list_values(head):
  result = []
  current_node = head
  while current_node:
    result.append(current_node.val)
    current_node = current_node.next
  return result
  
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

print(linked_list_values(a)) # -> [ 'a', 'b', 'c', 'd' ]

# Alvin's Solution

def linked_list_Alvin_iterative(head):
  values = []
  current = head
  while current is not None:
    values.append(current.val)
    current = current.next
  return values

print('Iterative', linked_list_Alvin_iterative(a)) # -> [ 'a', 'b', 'c', 'd' ]

def linked_list_Alvin_recursive(head):
  values = []
  fill_values(head, values)
  return values

def fill_values(head, values):
  if head is None:
    return
  values.append(head.val)
  fill_values(head.next, values)