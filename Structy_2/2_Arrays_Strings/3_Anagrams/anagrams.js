const anagrams = (s1, s2) => {
  // todo
  if(s1.length != s2.length){
    return false
  }
  let obj1 = {}
  let obj2 = {}
  
  for( let char of s1){
    if(!obj1[char]){
      obj1[char] = 1
    }
    obj1[char] += 1
  }

 for( let char of s2){
    if(!obj2[char]){
      obj2[char] = 1
    }
    obj2[char] += 1
  }

 for (let key in obj1){
   if(obj2[key] === obj1[key]){
     continue
   }
   else{
     return false
   }
 }
  
  return true
  
};

// anagrams('restful', 'fluster'); // -> true
anagrams('cats', 'tocs'); // -> false