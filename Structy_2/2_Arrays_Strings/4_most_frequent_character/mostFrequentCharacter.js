const mostFrequentChar = (s) => {
  const obj = {}
  
  for (let char of s){
    if(!obj[char]){
      obj[char] = 1
    }
    else{
      obj[char] += 1
    }
  }
  let max = 0
  let result;
  for(let key in obj){
    if(obj[key] > max){
      max = obj[key]
      result = key
    }
  }
  return result
  
};
