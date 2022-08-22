const pairProduct = (numbers, targetProduct) => {
  // todo
  let previousNumbers = {}
  
  for(let i = 0; i < numbers.length; i++){
    let num = numbers [i]
    let complement = targetProduct/num
    if(complement in previousNumbers) return [i, previousNumbers[complement]]
    previousNumbers[num] = i
    console.log(previousNumbers)
    }
  }


console.log(pairProduct([3, 2, 5, 4, 1], 8))
