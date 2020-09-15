#!/usr/bin/node
// export a function
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
