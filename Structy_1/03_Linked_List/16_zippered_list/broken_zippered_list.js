class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const zipperLists = (head1, head2) => {
  let current1 = head1
  let current2 = head2
  
  while(current1 && current2){
    let next1 = current1.next
    let next2 = current2.next
    
    current1.next = current2
    current2.next = next1
    console.log(current1.next)
    console.log(current2.next)
    current1 = next1
    current2 = next2
    
  }
  console.log("2 Current", current2)
  console.log("2 NEXT", current2.next)
  console.log("1 current", current1)
  
  if(current1){
    console.log("HERE")
    
  }
  
  if(current2){
     
  }
  
//   while(current2){
    
    
//     let next = current2.next
//     current2.next = next
//     current2 = next
//   }
  
  return head1
  
};

const s = new Node("s");
const t = new Node("t");
s.next = t;
// s -> t

const one = new Node(1);
const two = new Node(2);
const three = new Node(3);
const four = new Node(4);
one.next = two;
two.next = three;
three.next = four;
// 1 -> 2 -> 3 -> 4

zipperLists(s, one);
// s -> 1 -> t -> 2 -> 3 -> 4


/* GOT STUCK SO ALVIN'S CODE BELOW */