class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}



const mergeLists = (head1, head2) => {
  let tail = head1
  let current1 = head1
  let current2 = head2
  console.log("SUPER NEXT", current1.next)
  
  while (current1 !== null && current2 !== null){
    console.log("first", current1)
    console.log("second", current2)
    debugger
     if (current1.val < current2.val){
       console.log("tail", tail)
       tail.next = current1
      //  I'm taking head1 and making it head1 again!!!
      // So I'm really just setting current1.next to itself over and over again
      // Have to add the dummy Head!
      console.log("NEXT", current1.next)
       current1 = current1.next
       console.log("NEXT", current1.next)
    }
    else{
       tail.next = current2
       current2 = current2.next
    }
    tail = tail.next
  }
  
  if(current1 !== null) tail.next = current1
  if(current2 !== null) tail.next = current2
  
  return
  
};


const a = new Node(5);
const b = new Node(7);
const c = new Node(10);
const d = new Node(12);
const e = new Node(20);
const f = new Node(28);
a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;
// 5 -> 7 -> 10 -> 12 -> 20 -> 28

const q = new Node(6);
const r = new Node(8);
const s = new Node(9);
const t = new Node(25);
q.next = r;
r.next = s;
s.next = t;
// 6 -> 8 -> 9 -> 25

mergeLists(a, q);