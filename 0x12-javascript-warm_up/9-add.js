#!/usr/bin/node

const args = process.argv.slice(2);
const n1 = Number(args[0]);
const n2 = Number(args[1]);

if (isNaN(n1) || isNaN(n2)) {
  console.log('NaN');
} else {
  console.log(add(n1, n2));
}

function add (a, b) {
  return a + b;
}
