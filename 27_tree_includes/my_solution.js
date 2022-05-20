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
