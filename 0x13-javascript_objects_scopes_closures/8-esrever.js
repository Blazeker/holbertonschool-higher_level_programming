#!/usr/bin/node
// Return the reversed version of a list

exports.esrever = function (list) {
  let end = list.length - 1;
  for (let begin = 0; begin <= end; begin++) {
    const temp = list[begin];
    list[begin] = list[end];
    list[end] = temp;
    end--;
  }
  return (list);
};
