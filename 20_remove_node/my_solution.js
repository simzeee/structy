class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const removeNode = (head, targetVal) => {
  // todo
  
  if(head.val === targetVal){
    let newHead = head.next
    head.next = null
    return newHead
  }
  
  let current = head
  let prev = null

  while(current){
    if(current.val === targetVal){
      console.log("HI")
      let newNode = current.next
      prev.next = current.next
      current.next = null
      current = newNode
      return head
    }
      prev = current
      current = current.next
  }
};