#!/usr/bin/node
// read content from a file
const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
