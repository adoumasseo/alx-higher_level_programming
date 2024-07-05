#!/usr/bin/node
const Rectangle = require('./5-square.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const printer = c || 'X';
    let figure = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        figure += printer;
      }
      if (i !== this.height - 1) {
        figure += '\n';
      }
    }
    console.log(figure);
  }
}
module.exports = Square;
