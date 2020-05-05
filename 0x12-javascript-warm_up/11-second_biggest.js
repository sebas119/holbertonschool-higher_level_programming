#!/usr/bin/node

const args = process.argv.slice(2);

function secondBig (args) {
  let first = Number.NEGATIVE_INFINITY;
  let second = Number.NEGATIVE_INFINITY;

  for (const arg of args) {
    if (Number(arg) > first) {
      second = first;
      first = arg;
    } else if (Number(arg) > second || second === first) {
      second = arg;
    }
  }
  return second;
}

if (args.length <= 1) {
  console.log(0);
} else {
  console.log(secondBig(args));
}
