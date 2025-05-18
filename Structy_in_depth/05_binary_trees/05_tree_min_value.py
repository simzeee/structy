class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_min_value(root, smallest=float("inf")):
    if root is None:
        return smallest

    if root.val < smallest:
        smallest = root.val

    left_values = tree_min_value(root.left, smallest)
    right_values = tree_min_value(root.right, smallest)
    print(left_values, right_values)
    return min(left_values, right_values)


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
print(tree_min_value(a))  # -> -2

# better version


def tree_min_value(root, smallest=float("inf")):
    if root is None:
        return smallest

    left_values = tree_min_value(root.left, smallest)
    right_values = tree_min_value(root.right, smallest)

    return min(root.val, left_values, right_values)
