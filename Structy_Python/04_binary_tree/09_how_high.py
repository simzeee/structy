def how_high(node):
    if node is None:
        return -1

    left_tree_height = how_high(node.left)
    right_tree_height = how_high(node.right)

    return 1 + max(left_tree_height, right_tree_height)
