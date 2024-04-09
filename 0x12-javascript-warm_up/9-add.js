#!/usr/bin/node
function add (a, b) {
  a = parseInt(process.argv[2]);
  b = parseInt(process.argv[3]);
  if (a && b) {
    console.log(a + b);
  } else { console.log('NaN'); }
}
add();
