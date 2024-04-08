#!/usr/bin/node
const myVar = parseInt(process.argv[2]);
if (!process.argv[2]) {
  console.log('Not a number');
} else if (!myVar) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myVar);
}
