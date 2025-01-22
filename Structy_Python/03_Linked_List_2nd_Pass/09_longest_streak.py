def longest_streak_mine(head):
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


def longest_streak(head):
    max_streak = 0
    current_streak = 0
    current_node = head
    prev_val = None

    while current_node is not None:
        if current_node.val == prev_val:
            current_streak += 1
        else:
            current_streak = 1

        prev_val = current_node.val
        if current_streak > max_streak:
            max_streak = current_streak

        current_node = current_node.next

    return max_streak
