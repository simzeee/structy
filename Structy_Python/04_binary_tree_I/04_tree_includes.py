def tree_includes(root, target):
    if root is None:
        return False

    stack = [root]

    while stack:
        current = stack.pop()

        if current.val == target:
            return True

        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

    return False
