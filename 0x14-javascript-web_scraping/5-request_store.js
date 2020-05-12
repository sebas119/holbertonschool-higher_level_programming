#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    if (response && response.statusCode === 200) {
      fs.writeFile(process.argv[3], body, (err, data) => {
        if (err) {
          console.log(err);
        }
      });
    }
  }
});
