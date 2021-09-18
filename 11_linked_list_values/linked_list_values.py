class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

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
