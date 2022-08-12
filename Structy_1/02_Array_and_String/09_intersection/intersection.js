// Brute force solution
const intersection = (a, b) => {
  const result = []
for(let num of a){
  if(b.includes(num)){
    result.push(num)
  }
}
  return result
};

// set demo

const mySet = new Set();
mySet.add(3)
mySet.add(5)
mySet.add(3)
console.log(mySet)
console.log(mySet.has(3))
console.log(mySet.has(12))
console.log(mySet.has(5))

// lookup time in a set is constant time O(1)

const intersectionTwo = (a,b) => {

const result = []

const items = new Set();

for(let item of a){
  items.add(item); // also constant time
}

for (let el of b){
  if(items.has(el)){
    result.push(el)
  }
}

return result

// two loops, but not nested

}