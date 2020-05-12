#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

request(`https://swapi-api.hbtn.io/api/films/${movieId}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    if (response && response.statusCode === 200) {
      console.log(JSON.parse(body).title);
    }
  }
});
