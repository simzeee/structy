class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const treeSum = (root) => {
  if(root === null) return 0
  
  let queue = [root]
  let result = []
  
  while(queue.length > 0){
    let current = queue.pop()
    result.push(current.val)
    if(current.left) queue.unshift(current.left)
    if(current.right) queue.unshift(current.right)
  }
  
  return result.reduce(((a, b) => a + b),0)
  
};


// const treeSum = (root) => {
  
// }

const a = new Node(3);
const b = new Node(11);
const c = new Node(4);
const d = new Node(4);
const e = new Node(-2);
const f = new Node(1);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//       3
//    /    \
//   11     4
//  / \      \
// 4   -2     1

console.log(treeSum(a)); // -> 21















module.exports = {
  treeSum
};

