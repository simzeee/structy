class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const breadthFirstValues = (root) => {
  // use a queue
  if(root === null){
    return []
  }
  let queue = [root]
  // let current = root
  let result = []
  
  while(queue.length != 0) {
    let current = queue.pop()
    result.push(current.val)
    if(current.left) queue.unshift(current.left)
    if(current.right) queue.unshift(current.right)
  }
  
  return result
  
};

const a = new Node('a');
const b = new Node('b');
const c = new Node('c');
const d = new Node('d');
const e = new Node('e');
const f = new Node('f');

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f

breadthFirstValues(a); 
//    -> ['a', 'b', 'c', 'd', 'e', 'f']
