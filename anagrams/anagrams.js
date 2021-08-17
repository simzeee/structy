// My broken solution
// const anagrams = (s1, s2) => {
//   let o1 = {};
//   let o2 = {};

//   for (let c in s1) {
//     if (!o1[s1[c]]) {
//       o1[s1[c]] = 1;
//     } else {
//       o1[s1[c]] += 1;
//     }
//   }

//   for (let c in s2) {
//     if (!o2[s2[c]]) {
//       o2[s2[c]] = 1;
//     } else {
//       o2[s1[c]] += 1;
//     }
//   }
//   console.log(o1);
//   console.log(o2);
//   console.log(o2["a"]);

//   // let count1 = 0
//   // let count2 = 0
//   for (key in o1) {
//     console.log(key);
//     if (o2[key] === undefined) {
//       return false;
//     }
//   }

//   return true;
// };

// This worked!

const anagrams = (s1, s2) => {
  let o1 = {};
  let o2 = {};

  if(s1.length != s2.length){
    return false
  }

  for (let c in s1) {
    if (!o1[s1[c]]) {
      o1[s1[c]] = 1;
    } else {
      o1[s1[c]] += 1;
    }
  }

  for (let char in s2) {
    // console.log(o2)
    // console.log(s2[char])
    if (!o2[s2[char]]) {
      o2[s2[char]] = 1;
    } else {
      o2[s2[char]] += 1;
    }
  }
  // console.log(o1);
  // console.log(o2);
  for (key in o1) {
    // console.log(key);
    if (o2[key] === undefined || o2[key] != o1[key]) {
      return false;
    }
  }

  return true;
};

// console.log(anagrams('restful', 'fluster'))
// console.log(anagrams('cats', 'tocs'));
// console.log(anagrams('monkeyswrite', 'newyorktimes'));
// console.log(anagrams('paper', 'reapa'));

// Alvin's Solution

const anagrams = (s1, s2) => {
  const count = {};
  for (let char of s1) {
    if (!(char in count)) {
      count[char] = 0;
    }
    count[char] += 1;
  }
  
  for (let char of s2) {
    if (count[char] === undefined) {
      return false;
    } else {
      count[char] -= 1;
    }
  }
  
  for (let char in count) {
    if (count[char] !== 0) {
      return false;
    }
  }
  
  return true;
};