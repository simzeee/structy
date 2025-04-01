# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


def depth_first_iterative_tree_levels(root):
    if root is None:
        return []

    levels = []
    stack = [(root, 0)]

    while stack:
        node, level_num = stack.pop()

        if len(levels) == level_num:
            levels.append([node.val])
        else:
            levels[level_num].append(node.val)

        if node.right is not None:
            stack.append((node.right, level_num + 1))
        if node.left is not None:
            stack.append((node.left, level_num + 1))

    return levels


from collections import deque


def breadth_first_iterative_tree_levels(root):
    if root is None:
        return []

    levels = []
    queue = deque([(root, 0)])

    while queue:
        node, level_num = queue.popleft()

        if len(levels) == level_num:
            levels.append([node.val])
        else:
            levels[level_num].append(node.val)

        if node.left is not None:
            queue.append((node.left, level_num + 1))
        if node.right is not None:
            queue.append((node.right, level_num + 1))

    return levels


def recursive_tree_levels(root):
    levels = []
    fill_levels(root, levels, 0)
    return levels


def fill_levels(root, levels, level_num):
    if root is None:
        return

    if len(levels) == level_num:
        levels.append([root.val])
    else:
        levels[level_num].append(root.val)

    fill_levels(root.left, levels, level_num + 1)
    fill_levels(root.right, levels, level_num + 1)
