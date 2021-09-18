// My Solution
const mostFrequentChar = (s) => {
  
  const count = {}
  
  for (let char of s){
    if(!(char in count)){
      count[char] = 1
    }
    count[char] += 1
  }
 
  let values = Object.values(count)
  values.sort().reverse()
  for(key in count){
    if(count[key]===values[0])
      {return key}
  }
  
};

mostFrequentChar('bookeeper');

// Alvin's Solution

const mostFrequentChar = (s) => {
  const count = {};
  
  for (let char of s) {
    if (!(char in count)) {
      count[char] = 0;
    }
    count[char] += 1
  }
  
  let best = null;
  for (let char of s) {
    if (best === null || count[char] > count[best]) {
      best = char;
    }
  }
  return best;
};