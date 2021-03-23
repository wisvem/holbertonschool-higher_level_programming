#!/usr/bin/node
const args = process.argv;
let smax = 0;
if (args.length >= 4) {
  const myArray = args.slice(2, args.length);
  myArray.sort();
  smax = myArray[myArray.length - 2];
}
console.log(smax);
