#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    if (response && response.statusCode === 200) {
      const results = JSON.parse(body).results;
      let counter = 0;
      let found;
      for (const data of results) {
        found = data.characters.find((n) => {
          return n.endsWith('/18/');
        });
        if (found !== undefined) counter++;
      }
      console.log(counter);
    }
  }
});
