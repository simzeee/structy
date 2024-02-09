class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def longest_streak(head):
    max_streak = 0
    current_streak = 0
    if head is not None:
        prev_val = head.val
    current = head

    while current is not None:
        if current.val == prev_val:
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
        else:
            current_streak = 1
            prev_val = current.val
        current = current.next

    return max_streak


a = Node(9)
b = Node(9)
c = Node(1)
d = Node(9)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 9 -> 9 -> 1 -> 9 -> 9 -> 9

print(longest_streak(a))  # 3
