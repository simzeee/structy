class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_value_count(root, target):

    if root is None:
        return 0

    count = 0
    stack = [root]

    while stack:
        current = stack.pop()
        if current.val == target:
            count += 1
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return count
