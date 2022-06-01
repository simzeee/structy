class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const levelAverages = (root) => {

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
  
  // return levels
  let result = []
  for (let level of levels){
    result.push(avg(level))
  }
  return result
  // levels.forEach(item => result.push(item.reduce(function(acc, val) { return (acc + val); }, 0)))
   

};

const avg = (array) => {
  let sum = 0;
  for (let num of array) {
    sum += num;
  }
  return sum / array.length;
};

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

console.log(levelAverages(a)); // -> [ 3, 7.5, 1 ] 