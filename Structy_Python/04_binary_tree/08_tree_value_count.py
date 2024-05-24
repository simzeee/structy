from collections import deque


def tree_value_count_iterative(root, target):
    if root is None:
        return 0

    stack = [root]
    count = 0

    while stack:
        current = stack.pop()
        if current.val == target:
            count = count + 1

        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

    return count


def tree_value_count_recursive(root, target):
    if root is None:
        return 0

    match = 1 if root.val == target else 0

    return (
        match
        + tree_value_count_recursive(root.left, target)
        + tree_value_count_recursive(root.right, target)
    )


def tree_value_count_iterative_breadth_first(root, target):
    if root is None:
        return 0

    count = 0
    queue = deque([root])

    while queue:
        current = queue.popleft()

        if current.val == target:
            count += 1

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return count
