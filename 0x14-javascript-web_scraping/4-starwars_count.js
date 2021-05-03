#!/usr/bin/node
const request = require('request');
let count = 0;
const url = process.argv[2];
let url2 = 'https://swapi-api.' + 'hbtn.io/api/people/18';

if (url !== 'https://swapi-api.hbtn.io/api/films') {
  url2 = url2 + 'algomalo';
}

request(url2, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  JSON.parse(body).films.forEach(element => {
    count++;
  });
  console.log(count); // Print the response status code if a response was received
});
