#!/usr/bin/node
const myVar = parseInt(process.argv[2]);
if (!myVar) {
  console.log('Missing size');
}
const strng = 'X';
for (let i = 0; i < myVar; i++) {
  console.log(strng.repeat(myVar));
}
