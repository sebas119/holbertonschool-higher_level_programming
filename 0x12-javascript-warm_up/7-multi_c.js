#!/usr/bin/node

const args = process.argv.slice(2);
const str = 'C is fun';
const n = Number(args[0]);

if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < n; i++) {
    console.log(str);
  }
}
