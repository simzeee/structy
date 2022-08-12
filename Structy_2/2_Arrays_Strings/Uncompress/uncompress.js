const uncompress = (s) => {
  // todo
  let result = [];
  let nums = '0123456789'
  
  let i = 0;
  let j = 0;
  while(j < s.length){
    if(nums.includes(s[j])){
      j +=1
    } else{
      const num = Number(s.slice(i,j));
      for (let count = 0; count < num; count += 1){
        result.push(s[j])
      }
      j+=1;
      i = j;
    }
  }
  return result.join('');
};