// {
//   "query": "mutation{  login(email: \"{{form1.email}}\", password: \"{{form1.password}}\") {    id  }}"
// }

const myObject = {
  "query": "mutation{  login(email: \"{{form1.email}}\", password: \"{{form1.password}}\") {    id  }}"
}

const toDos = [
  { id: 1, text: "Learn APIS" },
  { id: 2, text: "Build APIS" },
  { id: 3, text: "Profit" },
];

// console.log(toDos.indexOf('{id: 1, text: "Learn APIS"}'))

// toDos.splice(toDos[index])

toDos.forEach(function(toDo, i){
  if(toDo.id === 3){
    toDos.splice(i, 1)
  }
})

console.log(toDos)