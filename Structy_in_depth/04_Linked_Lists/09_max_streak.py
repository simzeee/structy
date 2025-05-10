class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def longest_streak(head):
    if head is None:
        return 0
    streak = []
    counter = 0
    current = head
    compare = head.val

    while current is not None:
        if current.val == compare:
            compare = current.val
            counter += 1
        else:
            streak.append(counter)
            counter = 1
            compare = current.val
        current = current.next
    streak.append(counter)
    return max(streak)
