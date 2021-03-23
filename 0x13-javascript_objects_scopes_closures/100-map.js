#!/usr/bin/node
const list = require('./100-main').list;
const map1 = list.map(x => x * list.indexOf(x));
console.log(list);
console.log(map1);
