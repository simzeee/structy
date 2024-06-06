from collections import deque


def depth_first_iterative_print(graph, start):
    stack = [ start ]
    while len(stack) > 0:
        current = stack[-1]
        print(current)
        stack.pop()
        for neighbor in graph[current]:
            stack.append(neighbor)


def depth_first_recursive_print(graph, current):
    print(current)
    for neighbor in graph[current]:
        depth_first_recursive_print(graph, neighbor)


def breadth_first_print(graph, start):
    queue = deque([start])
    while len(queue) > 0:
        current = queue[0]
        print(current)
        queue.popleft()
        for neighbor in graph[current]:
            queue.append(neighbor)


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

depth_first_iterative_print(graph, "a")
depth_first_recursive_print(graph, "a")
breadth_first_print(graph, "a")
