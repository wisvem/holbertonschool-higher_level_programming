#!/usr/bin/node
const request = require('request');
let count = 0;
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const result = JSON.parse(body).results;

  result.forEach(element => {
    element.characters.forEach(c => {
      if (c.includes('18')) {
        count++;
      }
    });
  });
  console.log(count);
});
