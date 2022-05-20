class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const addLists = (head1, head2, carry = 0) => {
  // todo
   if (head1 === null && head2 === null && carry === 0) return null;
  
  const val1 = head1 === null ? 0 : head1.val;
  const val2 = head2 === null ? 0 : head2.val;
  
  const sum = val1 + val2 + carry;
  const nextCarry = sum > 9 ? 1 : 0;
  const digit = sum % 10;
  const result = new Node(digit);
  
  const next1 = head1 === null ? null : head1.next
  const next2 = head2 === null ? null : head2.next
  
  result.next = addLists(next1, next2, nextCarry);
  
  return result;
  
  
};

