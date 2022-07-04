const depthFirstPrintIterative = (graph, source) => {
  const stack = [source];

  while (stack.length > 0) {
    const current = stack.pop();
    console.log(current);
    for (let neighbor of graph[current]) {
      stack.push(neighbor);
    }
  }
};

const depthFirstPrintRecursive = (graph, source) => {
  console.log(source);
  for (let neighbor of graph[source]) {
    depthFirstPrintRecursive(graph, neighbor);
  }
};

const breadthFirstPrintIterative = (graph, source) => {
  const queue = [source];
  while (queue.length > 0) {
    const current = queue.shift()
    console.log(current);
    for (let neighbor of graph[current]) {
      queue.push(neighbor)
    }
  }
};

const graph = {
  a: ["c", "b"],
  b: ["d"],
  c: ["e"],
  d: ["f"],
  e: [],
  f: [],
};

// depthFirstPrintIterative(graph, "a");
// depthFirstPrintRecursive(graph, "a")
breadthFirstPrintIterative(graph, "a");
