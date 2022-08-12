const treeLevels = (root) => {
  // todo
  if (root === null) return [];
 
  const levels = []
  const queue = [{node: root, levelNum: 0}]
  
  while(queue.length > 0) {
    
    const {node, levelNum} = queue.shift()
    
    if(levels.length === levelNum){
      levels[levelNum] = [node.val]
    } else {
      levels[levelNum].push(node.val);
    }
    
    if (node.left !== null) queue.push({ node: node.left, levelNum: levelNum + 1 });
    if (node.right !== null) queue.push({ node: node.right, levelNum: levelNum + 1 });
    
  }
  
  return levels;
};
