# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# def tree_sum(root):
#   if not root:
#     return 0

#   stack = [root]
#   sum = 0

#   while stack:
#     current = stack.pop(0)
#     sum += current.val

#     if current.left:
#       stack.append(current.left)
#     if current.right:
#       stack.append(current.right)

#   return sum

# def tree_sum_recursion(root):
#   if root is None:
#     return 0

#   return root.val + tree_sum(root.left) + tree_sum(root.right)

from collections import deque


def tree_sum(root):
    if not root:
        return 0

    queue = deque([root])
    total_sum = 0

    while queue:
        node = queue.popleft()

        total_sum += node.val

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return total_sum
