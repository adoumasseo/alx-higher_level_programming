#!/usr/bin/node
exports.esrever = function (list) {
  const myNewArray = [];
  for (let i = list.length - 1; i >= 0; i--) {
    myNewArray.push(list[i]);
  }
  return myNewArray;
};
