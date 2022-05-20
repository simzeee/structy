class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}
// My solution
const sumList = (head) => {
  let current_node = head
  let sum = 0
  while(current_node){
    sum += current_node.val
    current_node = current_node.next
  }
  return sum
};


// Recursive Solution

const sumList = (head) => {
  if (head === null) return 0;
  return head.val + sumList(head.next)
}