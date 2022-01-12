// Iterative

const isUnivalueList = (head) => {
  let current = head;
  
  while (current !== null) {
    if (current.val !== head.val) return false;
    current = current.next;
  }
  
  return true;
}

// Recursive

const isUnivalueList = (head, prevVal = null) => {
  if (head === null) return true;
  if (prevVal === null || prevVal === head.val) {
    return isUnivalueList(head.next, head.val);
  } else {
    return false;
  }
}