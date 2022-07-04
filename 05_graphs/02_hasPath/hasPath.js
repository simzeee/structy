const hasPath = (graph, src, dst) => {
  // todo
  const stack = [ src ];
  
  while (stack.length > 0) {
    const current = stack.pop()
    if(current === dst) return true
    for (let neighbor of graph[current]) {
      stack.push(neighbor)
    }
  }
  return false
  
};

