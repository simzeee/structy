class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_values(head, values=None):
    if values is None:
        values = []
    if head is None:
        return values
    values.append(head.val)
    return linked_list_values(head.next, values)


# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# print(linked_list_values(a)) # -> [ 'a', 'b', 'c', 'd' ]
