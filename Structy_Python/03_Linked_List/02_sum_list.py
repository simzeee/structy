# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None


def sum_list(head):
    sum = 0
    current = head
    while current is not None:
        sum = sum + current.val
        current = current.next

    return sum


def recursive_sum_list(head):
    sum = [0]  # Use a list to store the sum
    add_sum(head, sum)
    print("sum_list", sum[0])
    return sum[0]


def add_sum(head, sum):
    if head is None:
        return
    sum[0] += head.val  # Update the value inside the list
    print("sum", sum[0])
    add_sum(head.next, sum)


# Alvin's recursive:


def sum_list_recusion_alvin(head):
    if head is None:
        return 0
    return head.val + sum_list(head.next)
