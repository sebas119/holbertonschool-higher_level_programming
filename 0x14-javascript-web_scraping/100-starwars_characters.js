#!/usr/bin/node

const request = require('request');

const opCharacters = {
  url: `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`
};

request.get(opCharacters, (error, response, body) => {
  if (!error) {
    const charUrls = JSON.parse(body).characters;
    printNames(charUrls, 0);
  }
});

const printNames = (charUrls, index) => {
  request.get(charUrls[index], (error, response, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < charUrls.length) {
        printNames(charUrls, index + 1);
      }
    }
  });
};
