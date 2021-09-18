class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const linkedListValues = (head) => {
  let result = []
  let currentNode = head
  while (currentNode){
    result.push(currentNode.val)
    currentNode = currentNode.next
  }
  return result
};

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");

a.next = b;
b.next = c;
c.next = d;

// a -> b -> c -> d

console.log(linkedListValues(a)); // -> [ 'a', 'b', 'c', 'd' ]