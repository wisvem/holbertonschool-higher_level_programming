#!/usr/bin/node
const file = process.argv.slice(2)[0]
fs = require('fs')
fs.readFile(file, 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
