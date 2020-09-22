#!/usr/bin/node
// write content to a file
const fs = require('fs');
const file = process.argv[2];
const data = process.argv[3];
fs.writeFile(file, data, function (err) {
  if (err) return console.log(err);
});
