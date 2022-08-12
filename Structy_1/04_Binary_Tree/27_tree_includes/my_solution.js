const treeIncludes = (root, target) => {
  // todo
  if(root === null){
    return false
  }
  let stack = [root]
  let result = []
  while(stack.length > 0){
    
    let current = stack.pop()
    console.log(current)
    if(current.val === target){
      return true
    }
    result.push(current.val)
    if(current.right) stack.push(current.right)
    if(current.left) stack.push(current.left)
  }
  
  return false
  
};

const treeIncludesBreadth = (root, target) => {
  // breadth first traversal
  if(root === null){return false}
  const queue = [root]
  while(queue.length > 0) {
    const current = queue.shift();
    // console.log(current.val)
    if(current.val === target){
      return true
    }
    if(current.left) queue.push(current.left);
    if(current.right) queue.push(current.right);
  }
  
  return false
  
}


const treeIncludesRecursive = (root, target) => {
   if(root === null){
    return false
  }
  if(root.val === target){
    return true
  }
  return treeIncludes(root.left, target) || treeIncludes(root.right, target)
}
