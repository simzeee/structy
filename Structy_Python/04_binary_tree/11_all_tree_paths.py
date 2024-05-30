def all_tree_paths(root):
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [[root.val]]

    paths = []

    left_sub_paths = all_tree_paths(root.left)

    for sub_path in left_sub_paths:
        paths.append([root.val, *sub_path])

    right_sub_paths = all_tree_paths(root.right)

    for sub_path in right_sub_paths:
        paths.append([root.val, *sub_path])

    return paths
