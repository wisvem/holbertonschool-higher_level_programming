#!/usr/bin/node
const argv = process.argv;
let smax = 0;
if (argv.length >= 4) {
  const myArray = argv.slice(2, argv.length);
  myArray.sort();
  smax = myArray[myArray.length - 2];
}
console.log(smax);
