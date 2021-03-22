#!/usr/bin/node
const args = process.argv;
const myNum = Number(args[2]);
if (isNaN(myNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < myNum; index++) {
    console.log('C is fun');
  }
}
