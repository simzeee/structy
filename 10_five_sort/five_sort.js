const fiveSort = (nums) => {
  let i = 0;
  let j = nums.length -1
  
  while (i <= j){
    if(nums[j] === 5){
      j--
    }
    else if(nums[i] === 5){
      // array destructuring
      [nums[i], nums[j]] = [nums[j], nums[i]]
    }
    else{
      i++
    }
  }
  return nums
};


console.log(fiveSort([5, 5, 5, 1, 1, 1, 4]))