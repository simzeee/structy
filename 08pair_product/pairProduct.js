// My Solution

const pairProduct = (numbers, targetProduct) => {
  
  for(let i = 0;i<numbers.length;i++){
    let num1 = numbers[i]
    for(let j = 1;j<numbers.length;j++){
      let num2 = numbers[j]
      console.log(num1, num2)
      if(num1 * num2 === targetProduct){
        return [i,j]
      }
    }
  }
};

// Solution after "approach" video

const pairProduct = (numbers, targetProduct) => {
  
  previous = {}
//   the keys will be numbers of input array,
//   values will be indices where I can find numbers
  for(let i = 0;i<numbers.length;i++){
    let num = numbers[i]
    let complement = targetProduct/num
    if(complement in previous) return [previous[complement],i]
    
    previous[num] = i

  }
};