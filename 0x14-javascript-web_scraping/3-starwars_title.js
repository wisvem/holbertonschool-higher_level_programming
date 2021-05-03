#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2)[0];
request(`https://swapi-api.hbtn.io/api/films/${url}`, function (error, response, body) {
  if (error) {
    return console.log(error);
  }

  console.log(JSON.parse(body).title); // Print the response status code if a response was received
});
