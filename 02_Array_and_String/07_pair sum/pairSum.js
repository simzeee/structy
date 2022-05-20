// My Solution (Alvin called it Naive)
for(let i =0;i<numbers.length;i++){
  for(let j=i+1;j<numbers.length;j++){
     if(numbers[j]+numbers[i]===targetSum){
    return [j,i]
  }
}
}

// Alvin's solution
const pairSum = (numbers, targetSum) => {
  
  const previous = {}
  
  for(let i = 0;i<numbers.length;i++){
    const num = numbers[i]
    const complement = targetSum - num
    
    if (complement in previous){
      return [i, previous[complement]]
    }
    // You have to check for the key first and then put it in the object
  previous[numbers[i]] = i

};
}
