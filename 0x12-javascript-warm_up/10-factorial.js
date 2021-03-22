#!/usr/bin/node
function factorial (a) {
  if (a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
const args = process.argv;
const myNum = Number(args[2]);
if (isNaN(myNum)) {
  console.log(1);
} else {
  const res = factorial(myNum);
  console.log(res);
}
