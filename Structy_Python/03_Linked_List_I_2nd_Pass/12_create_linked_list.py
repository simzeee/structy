class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linked_list(values):

    if len(values) == 0:
        return None

    head = Node(values[0])
    current = head

    for val in values[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node
    return head
