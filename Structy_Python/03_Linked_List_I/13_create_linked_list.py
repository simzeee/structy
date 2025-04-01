class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linked_list(values):

    dummyHead = Node(None)
    tail = dummyHead

    for v in values:
        current = Node(v)
        tail.next = current
        tail = tail.next

    return dummyHead.next
