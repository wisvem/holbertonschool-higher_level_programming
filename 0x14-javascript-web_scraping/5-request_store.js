#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  fs.writeFile(file, body, 'utf8', function (err) {
    if (err) {
      return console.log(err);
    }
  });
});
