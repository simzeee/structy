class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")

a.next = b
b.next = c
c.next = d


def printList(head):
    current = head

    while current is not None:
        print(current.val)
        current = current.next


printList(a)

# recursive


def print_list_recursive(head):
    if head is None:
        return
    print(head.val)
    print_list_recursive(head.next)


print_list_recursive(a)
