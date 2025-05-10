class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def zipper_lists(head_1, head_2):
    tail = head_1
    current_1 = head_1.next
    current_2 = head_2
    counter = 0

    while current_1 is not None and current_2 is not None:
        print("1", current_1.val, "2", current_2.val)
        if counter % 2 == 0:
            tail.next = current_2
            current_2 = current_2.next
        else:
            tail.next = current_1
            current_1 = current_1.next
        tail = tail.next
        counter += 1

    if current_1 is None:
        tail.next = current_2
    if current_2 is None:
        tail.next = current_1

    return head_1


a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

zipper_lists(a, x)
# a -> x -> b -> y -> c -> z
