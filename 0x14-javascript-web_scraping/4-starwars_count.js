#!/usr/bin/node
// script that prints the number of movies

const request = require('request');
const url = process.argv[2];
const w = 18;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).results;
    let count = 0;
    for (const film of data) {
      for (const character of film.characters) {
        if (character.includes(w)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
