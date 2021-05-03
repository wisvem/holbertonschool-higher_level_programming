#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2)[0];
request(`${url}`, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  console.log('code:', response.statusCode); // Print the response status code if a response was received
});
