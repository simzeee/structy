const maxValue = (nums) => {
  // todo
  let max = nums[0];
  nums.forEach(num => {
    if(num > max){
      max = num
    }
  })
  return max
};