#!/usr/bin/node
const file = process.argv.slice(2)[0];
const text = process.argv.slice(2)[1];
const fs = require('fs');
fs.writeFile(file, text, 'utf8', function (err) {
  if (err) {
    return console.log(err);
  }
});
