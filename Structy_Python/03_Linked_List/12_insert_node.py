class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_node(head, value, index):
    current = head
    previous = None
    counter = 0

    while current is not None:
        if counter == index:
            if previous is not None:
                print("current", current, "previous", previous)
                newNode = Node(value)
                newNode.next = current
                previous.next = newNode
            else:
                newNode = Node(value)
                newNode.next = head
                return newNode

        previous = current
        current = current.next
        counter += 1

    print(counter)
    if index == counter:
        print("previous", previous)
        newNode = Node(value)
        previous.next = newNode

    return head
