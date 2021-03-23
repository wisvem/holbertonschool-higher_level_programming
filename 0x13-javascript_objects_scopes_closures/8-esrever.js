#!/usr/bin/node
exports.esrever = function (list) {
  const myArray = [];
  for (let index = 0; index < list.length; index++) {
    myArray[index] = list[list.length - index - 1];
  }
  return myArray;
};
