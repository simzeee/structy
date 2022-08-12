class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const howHigh = (node) => {
  if(node === null) return -1;
 
  let leftPath = howHigh(node.left)
  let rightPath = howHigh(node.right)
  
  return 1 + Math.max(leftPath, rightPath)
};


// console.log(howHigh(a)); // -> 0
// console.log(howHigh(null)); // -> -1



