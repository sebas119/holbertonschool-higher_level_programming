#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const ans = {};
    for (const todo of todos) {
      if (todo.completed === true && ans[todo.userId] === undefined) {
        ans[todo.userId] = 1;
      } else if (todo.completed === true) {
        ans[todo.userId] += 1;
      }
    }
    console.log(ans);
  }
});
