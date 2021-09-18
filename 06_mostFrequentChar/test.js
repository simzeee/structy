function joinedLogger(level, sep) {
  return function f(...msg) {
    let result = [];
    msg.forEach((ob) => {
      // console.log(ob);
      // console.log(ob.level);
      if (ob.level >= level) {
        result.push(ob.text);
      }
    });
    // console.log(result.join(sep));
    return result.join(sep);
  };
}

const loggerFun = joinedLogger(10, ":")

console.log(loggerFun({level:11,text:"pradeep"},{level:5,text:"kumar"},{level:16,text:"reddy"}))

// function joinedLogger(level, sep) {
//   return function (...messages) {
//     let res = "";
//     for (let i = 0; i < messages.length - 1; i++) {
//       if (messages[i].level >= level) {
//         res += messages[i].text + sep;
//       }
//     }
//     if (messages[messages.length - 1].level >= level) {
//       res += messages[messages.length - 1].text;
//     } else {
//       res = res.slice(0, -sep.length);
//     }
//     ws.write(res);
//     return res;
//   };
// }
