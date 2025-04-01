def has_path_recursive(graph, src, dst):
    if src == dst:
        return True

    for neighbor in graph[src]:
        if has_path_recursive(graph, neighbor, dst) == True:
            return True

    return False


def has_path_iterative_depth(graph, src, dst):
    stack = [src]
    found_dst = False
    while len(stack) > 0:
        current = stack[-1]
        if current == dst:
            return True
        stack.pop()
        for neighbor in graph[current]:
            stack.append(neighbor)
    return found_dst


from collections import deque


def has_path_iterative_breadth(graph, src, dst):
    queue = deque([src])

    while queue:
        current = queue.popleft()

        if current == dst:
            return True

        for neighbor in graph[current]:
            queue.append(neighbor)
    return False
