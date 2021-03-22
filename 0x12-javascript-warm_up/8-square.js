#!/usr/bin/node
const args = process.argv;
const myNum = Number(args[2]);
if (isNaN(myNum)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < myNum; index++) {
    for (let index2 = 0; index2 < myNum; index2++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
