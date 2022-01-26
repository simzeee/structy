const longestStreak = (head) => {
  let maxStreak = 0
  let currentStreak = 0
  let prevVal = null
  let current = head

  while(current !== null){
    if(current.val === prevVal){
      currentStreak += 1
    }
    else{
      currentStreak = 1
    }
    
    if (currentStreak > maxStreak){
      maxStreak = currentStreak
    }
    
    prevVal = current.val
    current = current.next    
  }
  return maxStreak
};