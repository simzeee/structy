class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

// const recursiveTreeValueCount = (root, target) => {
//   // todo
//   if(root === null) return 0;
//   const match = root.val === target ? 1 : 0;
//   return match + treeValueCount(root.left, target) + treeValueCount(root.right, target)
// };

// const depthFirstTreeValueCount = (root, target) => {
  
//   if(root === null) return 0;
  
//   let counter = 0
//   let stack = [root]
  
//   while(stack.length > 0){
//     let current = stack.pop()
//     if(current.val === target){
//       counter += 1
//     }
    
//     if (current.left) stack.push(current.left)
//     if (current.right) stack.push(current.right)
//   }
  
//   return counter
  
// }

const breadthFirstTreeValueCount = (root, target) => {
  if (root === null) return 0;
  
  let counter = 0;
  let queue = [root];
  
  while(queue.length > 0){
    let current = queue.shift()
    if (current.val === target) counter += 1;
    
    if(current.left) queue.push(current.left)
    if(current.right) queue.push(current.right)
    
  }
  return counter
}

const a = new Node(12);
const b = new Node(6);
const c = new Node(6);
const d = new Node(4);
const e = new Node(6);
const f = new Node(12);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//      12
//    /   \
//   6     6
//  / \     \
// 4  6     12

treeValueCount(a,  12); // -> 2