class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const createLinkedList = (values) => {
  let dummyHead = new Node("dummy")
  let tail = dummyHead
  let i = 0
  
  while(i<values.length){
    tail.next = new Node(values[i])
    tail = tail.next
    i += 1
  }
  
  return dummyHead.next

};


console.log(createLinkedList(["a"]));
