#!/usr/bin/node
// print 3 lines
let number = process.argv.slice(2)[0];
number = parseInt(number);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
