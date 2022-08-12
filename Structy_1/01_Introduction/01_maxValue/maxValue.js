// My Solution

// const maxValue = (nums) => {
//   let max = nums[0];
//   for (let i = 1; i < nums.length; i++) {
//     if (nums[i] > max) {
//       max = nums[i];
//     }
//   }
//   return max;
// };

// Alvin's Solution

const maxValue = (nums) => {
  let maximum = -Infinity;

  for (let num of nums) {
    // iterates through number, not the indices
    if (num > maximum) maximum = num;
  }

  return maximum;
};

console.log(maxValue([1,2,3,4,5,]))

// n = length of array
// Time: O(n)
// Space: O(1)
