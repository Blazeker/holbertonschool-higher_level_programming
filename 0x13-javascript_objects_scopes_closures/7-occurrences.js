#!/usr/bin/node
// find the occurrences on a list

exports.nbOccurences = function (list, searchElement) {
  let reps = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) { reps++; }
  }
  return reps;
};
