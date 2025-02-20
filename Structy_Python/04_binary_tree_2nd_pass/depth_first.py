# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


def depth_first_values_iterative(root):
    if root is None:
        return []
    stack = [root]
    result = []

    while stack:
        current = stack.pop()
        result.append(current.val)

        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

    return result


def depth_first_values_recursive(root):
    if root is None:
        return []

    left_values = depth_first_values_recursive(root.left)
    right_values = depth_first_values_recursive(root.right)

    return [root, *left_values, *right_values]
