def tree_sum(root):
    if root is None:
        return 0
    sum = 0
    stack = [root]

    while stack:
        current = stack.pop()
        sum = sum + current.val

        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

    return sum


def tree_sum_recursive_depth_first(root):
    if root is None:
        return 0

    return root.val + tree_sum(root.left) + tree_sum(root.right)
