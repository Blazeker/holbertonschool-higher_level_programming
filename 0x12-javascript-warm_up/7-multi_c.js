#!/usr/bin/node
// print 3 lines
let times = process.argv.slice(2)[0];
times = parseInt(times);
if (isNaN(times)) {
  console.log('Missing number of ocurrences');
} else {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
}
