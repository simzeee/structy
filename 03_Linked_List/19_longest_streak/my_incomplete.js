
const longestStreak = (head) => {
  let current = head
  let current2 = head.next
  let tracker = {}
  
  
  while(current !== null){
    
    if(!tracker[current.val]){
      tracker[current.val] = 1
    }
    else{
      tracker[current.val] = tracker[current.val] + 1
    }
    current = current.next
  }
  
  const arr = Object.values(tracker)
  
  return Math.max(...arr)
  
};