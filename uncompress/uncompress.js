// This doesn't work if the integer is more than one digit
const uncompress = (s) => {
  let split = s.split("");

  let nums = [];
  let letter = [];

  for (let i = 0; i < split.length; i++) {
    if (Number(split[i])) {
      nums.push(split[i]);
    } else {
      letter.push(split[i]);
    }
  }
  let result = [];
  for (let i = 0; i < nums.length; i++) {
    result.push(letter[i].repeat(nums[i]));
  }
  return result.join("");
};
