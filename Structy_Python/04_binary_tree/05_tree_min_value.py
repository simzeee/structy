def tree_min_value(root):

    if root is None:
        return 0
    min = root.val
    stack = [root]

    while stack:
        current = stack.pop()
        if current.val < min:
            min = current.val

        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

    return min
