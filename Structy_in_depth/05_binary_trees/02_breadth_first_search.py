def breadth_first_values(root):
    if root is None:
        return []
    queue = [root]

    values = []

    while len(queue) > 0:
        current = queue.pop(0)
        values.append(current.val)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return values


from collections import deque


def breadth_first_values(root):
    if root is None:
        return []

    queue = deque([root])
    values = []

    while len(queue) > 0:
        current = queue.popleft()
        values.append(current.val)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return values
