const compress = (s) => {
  // todo
  let result = [];
  let i = 0;
  let j = 0;
  
  while(j <= s.length){    
    if(s[i] === s[j]){
      j += 1;
    }else {
    console.log(result)

      if(j-i > 1){
        result.push(String([j-i]), s[i]) 
      }
      else{
        result.push(s[i])
      }
      i = j
    }
  }
   return result.join("")
};

compress('ccaaatsss'); // -> '2c3at3s'