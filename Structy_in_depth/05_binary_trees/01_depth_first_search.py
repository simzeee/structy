def depth_first_values(root):

    if root is None:
        return []

    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)
    # return [root.val] + left_values + right_values
    return [root.val, *left_values, *right_values]


def depth_first_values(root):
    if not root:
        return []

    stack = [root]
    values = []

    while stack:
        node = stack.pop()
        values.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return values
