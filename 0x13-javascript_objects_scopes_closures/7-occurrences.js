#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  list.forEach((elt) => {
    if (elt === searchElement) { counter++; }
  });
  return counter;
};
