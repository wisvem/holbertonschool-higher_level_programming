#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
const userTasks = {};
let user = '';
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const result = JSON.parse(body);
  result.forEach(element => {
    if (user !== element.userId) {
      count = 0;
      user = element.userId;
    }
    if (element.completed === true) {
      userTasks[element.userId] = ++count;
    }
  });
  console.log(userTasks);
});
