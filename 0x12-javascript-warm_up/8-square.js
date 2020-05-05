#!/usr/bin/node

const args = process.argv.slice(2);
const n = Number(args[0]);

if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    let str = '';
    for (let j = 0; j < n; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
