#!/usr/bin/node
const dict = require('./101-data').dict;
const myDict = {};
for (const key in dict) {
  myDict[key] = [];
}
for (const key in dict) {
  myDict[dict[key]].push(key);
}
console.log(myDict);
