# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque


def breadth_first_values(root):
    if root is None:
        return []

    values = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        values.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return values
