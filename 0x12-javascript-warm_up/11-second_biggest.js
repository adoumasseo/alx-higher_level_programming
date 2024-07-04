#!/usr/bin/node
let greatest = parseInt(process.argv[2]);
let secondGreatest = parseInt(process.argv[2]);
const argc = process.argv;
if (argc.length <= 2) {
  console.log(0);
} else {
  for (let i = 2; i < argc.length; i++) {
    if (argc[i] > greatest) {
      secondGreatest = greatest;
      greatest = argc[i];
    }
  }
  console.log(secondGreatest);
}
