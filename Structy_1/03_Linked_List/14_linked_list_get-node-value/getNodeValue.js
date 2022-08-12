const getNodeValue = (head, index) => {
  let count = 0
  let current = head
  while(current){
    if(count === index){
      return current.val
    }
    count++
    current = current.next
  }
  return null
};

const getNodeValue = (head, index) => {
  if(index === 0){
    return head.val
  }
  if(head === null){
    return null
  }
  return getNodeValue(head.next, index -1)
}