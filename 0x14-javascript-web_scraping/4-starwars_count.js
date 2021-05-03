#!/usr/bin/node
const request = require('request');
let count = 0;
request('https://swapi-api.hbtn.io/api/people/18/', function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  JSON.parse(body).films.forEach(element => {
    count++;
  });
  console.log(count); // Print the response status code if a response was received
});
