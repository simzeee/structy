from statistics import mean


def level_averages(root):
    levels = []
    fill_levels(root, levels, 0)
    return [mean(level) for level in levels]


def fill_levels(root, levels, level_num):
    if root is None:
        return

    if len(levels) == level_num:
        levels.append([root.val])
    else:
        levels[level_num].append(root.val)

    fill_levels(root.left, levels, level_num + 1)
    fill_levels(root.right, levels, level_num + 1)
