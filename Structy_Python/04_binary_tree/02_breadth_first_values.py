from collections import deque

# Any recursive code requires the call stack and this traversal
# requires the queue. Iterative is the go to

# this is O(n^2)
def breadth_first_values_basic(root):
    # use a queue
    if root is None:
        return []

    queue = [root]
    values = []

    while queue:
        current = queue.pop(0)
        values.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return values


# this is O(n)
def breadth_first_values(root):
    if not root:
        return []

    queue = deque([root])
    values = []

    while queue:
        node = queue.popleft()

        values.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return values
