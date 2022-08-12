class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const treeMinValueDepth = (root) => {
//   depth first
  const stack = [root]
  let min = root.val
  while(stack.length > 0){
    let current = stack.pop()
    if(current.val < min){
      min = current.val
    }
    if(current.right) stack.push(current.right)
    if(current.left) stack.push(current.left)
  }
  return min
};

const treeMinValueBreadth = (root) => {
//   breadth first
  const queue = [root]
  let min = root.val
  
  while(queue.length != 0){
    let current = queue.shift()
    if(current.val < min){
      min = current.val
    }
    if(current.left) queue.push(current.left)
    if(current.right) queue.push(current.right)
  }
  
  return min
}