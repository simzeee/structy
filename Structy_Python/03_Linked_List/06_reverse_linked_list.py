class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head):
    current = head
    previous = None

    while current is not None:
        print("current", current.val)
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous


a = Node("a")
b = Node("b")
c = Node("c")


a.next = b
b.next = c


# a -> b -> c -> d -> e -> f

print(reverse_list(a))


def reverse_list_recursive(head, prev=None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    reverse_list_recursive(next, head)
