#!/usr/bin/node
// converter exercise

exports.converter = function (base) {
  return function (number) { return number.toString(base); };
};
