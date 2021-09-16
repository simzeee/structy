// Ryan and my solution
const compress = (s) => {
  let count = 1
  let current = s[0]
  let result = ""
  
  for (let i=0;i<s.length;i++){
    if(current === s[i+1]){
      count++
    }
    else {
      if (count>1){
       result += count 
      }
      result += current
      current = s[i+1]
      count = 1
    }
  }
  
  return result
  
};

// Pointer solution we came up with

const compress = (s) => {
  let i = 0
  let j = 0
  let result = ""
  
  while (j<s.length+1){
    if(s[j] ===s[i]){
      j++
    }
    else{
      let count = j - i
      if( count > 1){
       result += count 
      }
      result += s[i]
      i = j
      j++
    }
  }
    console.log(result)
    return result
  };