class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def longest_streak(head):
    if head is None:
        return 0

    max_streak = 0
    current_streak = 0
    current_node = head
    current_val = head.val

    while current_node is not None:
        print(current_node.val, current_streak, current_val)

        if current_node.val == current_val:
            current_streak += 1
        else:
            current_streak = 1
            current_val = current_node.val

        if current_streak > max_streak:
            max_streak = current_streak

        current_node = current_node.next

    return max_streak


a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 5 -> 5 -> 7 -> 7 -> 7 -> 6

longest_streak(a)  # 3
