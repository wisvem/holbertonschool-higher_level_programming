#!/usr/bin/node
const argv = process.argv;

function secondMax (myArray) {
  if (myArray.length <= 3) {
    return (0);
  }

  myArray = myArray.slice(2).map(n => parseInt(n));

  const max = Math.max(...myArray);

  const arr = myArray.filter(arr => arr < max);

  return (Math.max(...arr));
}

console.log(secondMax(argv));

/*
const args = process.argv;
let smax = 0;
if (args.length >= 4) {
  let mymyArray = args.slice(2, args.length);
  mymyArray.sort();
  smax = mymyArray[mymyArray.length - 1];
  mymyArray = mymyArray.filter(mymyArray => mymyArray < smax);
  smax = mymyArray[mymyArray.length - 1];
}
console.log(smax);
*/
