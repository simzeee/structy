# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def get_node_value(head, index):
#   tracker = 0
#   current = head
#   while current is not None:
#     print(current.val)
#     if tracker == index:
#       return current.val
#     tracker += 1
#     current = current.next
#   return None


# my solution
def get_node_value(head, index, tracker=0):
    if head is None:
        return None
    if tracker == index:
        return head.val
    return get_node_value(head.next, index, tracker=tracker + 1)


# Alvin


def get_node_value(head, index):
    if head is None:
        return None

    if index == 0:
        return head.val

    return get_node_value(head.next, index - 1)
