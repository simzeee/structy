class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_node(head, value, index):
    current = head
    prev = None
    count = 0
    insert = Node(value)

    if index == 0:
        insert.next = head
        return insert

    while current is not None:
        if index == count:
            prev.next = insert
            insert.next = current
            return head
        else:
            prev = current
            current = current.next
            count += 1
    if index == count:
        prev.next = insert
        return head
