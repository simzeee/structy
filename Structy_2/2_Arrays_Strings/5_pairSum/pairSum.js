const pairSum = (numbers, targetSum) => {
  let previousNumbers = {};

  for (let i = 0; i < numbers.length; i++) {
    let num = numbers[i]
    let complement = targetSum - num
    if(complement in previousNumbers) 
    {return [i, previousNumbers[complement]]}
    previousNumbers[num] = i
    console.log(previousNumbers)
  }
};

console.log(pairSum([1, 2, 3], 5));
