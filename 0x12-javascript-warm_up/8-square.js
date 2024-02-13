#!/usr/bin/node

let x = 0;

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  x = Number(process.argv[2]);
}

for (let i = 0; i < x; i++) {
  console.log('X' * x);
}
