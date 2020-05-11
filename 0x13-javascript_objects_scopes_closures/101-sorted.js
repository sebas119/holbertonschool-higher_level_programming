#!/usr/bin/node

const dict = require('./101-data').dict;

const ans = {};

for (const key in dict) {
  if (ans[dict[key]] === undefined) {
    ans[dict[key]] = [key];
  } else {
    ans[dict[key]].push(key);
  }
}

console.log(ans);
