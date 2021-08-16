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

// Ryan's Solution

while (j<s.length){
  let numbers = '0123456789'
  
  if(numbers.includes(s[j])){
//     This collects the integer value
    number += s[j]
  }
  else{
    for(let i = 0;i<Number(number);i++){
//       add integer many letters
      result += s[j]
      console.log(result)
    }
    number = ''
  }
  j++
  
}
return letter
};
