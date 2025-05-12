class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_node(head, value, index):
    new_node = Node(value)
    count = 0
    current = head

    prev = None

    if index == 0:
        new_node.next = head
        return new_node

    while current is not None:
        if index == count:
            prev.next = new_node
            new_node.next = current
            return head
        else:
            count += 1
            prev = current
            current = current.next

    if count == index:
        prev.next = new_node
        return head


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

insert_node(a, "m", 4)
# a -> b -> c -> d -> m
