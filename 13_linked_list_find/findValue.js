// class Node {
//   constructor(val) {
//     this.val = val;
//     this.next = null;
//   }
// }

// const linkedListFind = (head, target) => {
//   let currentNode = head
//   while(currentNode){
//      if(currentNode.val === target){
//     return true
//   }
//     currentNode = currentNode.next
//   }
// return false
// };

const linkedListFind = (head, target) => {
  if(!head){
    return false
  }
  else if(head.val === target){
    return true
  }
  else{
    return linkedListFind(head.next, target)
  }
}

// Alvin's Solutions

// const linkedListFind = (head, target) => {
//   let current = head;
//   while (current !== null) {
//     if (current.val === target) return true;
//     current = current.next;
//   }
//   return false;
// };

// const linkedListFind = (head, target) => {
//   if (head === null) return false;
//   if (head.val === target) return true;
//   return linkedListFind(head.next, target);
// };

