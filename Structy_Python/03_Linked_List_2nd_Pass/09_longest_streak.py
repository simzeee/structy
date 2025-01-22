class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def longest_streak(head):
    if head is None:
        return 0
    streak = {}
    current = head
    comparison_val = head.val

    while current is not None:
        current_val = current.val

        if current.val not in streak:
            streak[current.val] = 1
            comparison_val = current.val
        elif current_val == comparison_val:
            streak[current.val] += 1
        elif current_val != comparison_val and current_val in streak:
            streak[current_val] = 1
            comparison_val = current.val
        current = current.next

    return max(streak.values())


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

longest_streak(a)  # 3
