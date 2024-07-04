#!/usr/bin/node
let square = '';
const size = parseInt(process.argv[2]);
if (!size) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      square += 'X';
    }
    console.log(square);
    square = '';
  }
}
