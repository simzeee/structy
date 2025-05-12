class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_values(head):
    values = []
    return _linked_list_values(head, values)


def _linked_list_values(node, values_list):
    if node is None:
        return values_list
    values_list.append(node.val)
    return _linked_list_values(node.next, values_list)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_values(a))  # -> [ 'a', 'b', 'c', 'd' ]
