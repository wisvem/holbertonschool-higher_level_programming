#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const args = process.argv;
const myNum1 = Number(args[2]);
const myNum2 = Number(args[3]);
console.log(add(myNum1, myNum2));
