#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const userTasks = {};
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const result = JSON.parse(body);

  result.forEach(element => {
    if (element.completed === true) {
      if (userTasks[element.userId] === undefined) {
        userTasks[element.userId] = 1;
      } else {
        // add +1 to number of task
        userTasks[element.userId]++;
      }
    }
  });
  console.log(userTasks);
});
