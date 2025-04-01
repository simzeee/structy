# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


def depth_first_values(root):
    if root is None:
        return []
    values = []
    stack = [root]

    while stack:
        current = stack.pop()
        values.append(current.val)

        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

    return values

def recursive_depth_first(root):
    if root is None:
        return []
    
    left_values = recursive_depth_first(root.left)
    right_values = recursive_depth_first(root.right)

    return [ root.val, *left_values, *right_values]