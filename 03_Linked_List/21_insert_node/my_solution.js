class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const insertNode = (head, value, index) => {
  // todo
  const newNode = new Node(value)
  let current = head
  let counter = 0
  
  if(index === 0){
    newNode.next = head
    return newNode
  }

  while(current !== null){
    if(counter === index - 1){
      let nextNode = current.next
      current.next = newNode
      newNode.next = nextNode
    }
    current = current.next
    counter += 1
  }
  
  return head
};



const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");

a.next = b;
b.next = c;
c.next = d;

// a -> b -> c -> d

console.log(insertNode(a, 'x', 2));
// a -> b -> x -> c -> d
