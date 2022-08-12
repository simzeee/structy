// class Node {
//   constructor(val) {
//     this.val = val;
//     this.left = null;
//     this.right = null;
//   }
// }

const bottomRightValue = (root) => {
  // todo
  let queue = [root]
  let current = null;
  
  while(queue.length > 0){
    current = queue.shift()
    
    if(current.left) queue.push(current.left)
    if(current.right) queue.push(current.right)
    
  }
  
  return current.val
};
