
const allTreePaths = (root) => {
  // todo
  if(root === null) return []
  if(root.left === null && root.right === null){
    return [[root.val]]
  }
  const paths = [];
  
  const leftSubPaths = allTreePaths(root.left)
  for (let subPath of leftSubPaths){
    paths.push([root.val,...subPath])
  }
  
  const rightSubPaths = allTreePaths(root.right)
  for (let subPath of rightSubPaths){
    paths.push([root.val, ...subPath])
  }
  
  return paths
  
};

