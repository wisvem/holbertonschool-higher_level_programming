#!/usr/bin/node
const args = process.argv;
let smax = 0;
if (args.length >= 4) {
  let myArray = args.slice(2, args.length);
  myArray.sort();
  smax = myArray[myArray.length - 1];
  myArray = myArray.filter(myArray => myArray < smax);
  smax = myArray[myArray.length - 1];
}
console.log(smax);
