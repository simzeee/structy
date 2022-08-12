class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const isUnivalueList = (head) => {
  // todo
  const checker = {}
  let current = head
  
  while(current){
    if(!checker[current.val]){
      checker[current.val] = 1
    }
    else{
      checker[current.val] = checker[current.val]++
    }    
      current = current.next
  }
  
  // console.log(checker)
  
  return Object.keys(checker).length === 1
  
};

// const a = new Node(7);
// const b = new Node(7);
// const c = new Node(7);

// a.next = b;
// b.next = c;

// // 7 -> 7 -> 7

// console.log(isUnivalueList(a)); // true


