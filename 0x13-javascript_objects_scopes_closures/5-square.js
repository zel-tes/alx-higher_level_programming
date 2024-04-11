#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size, size1, size2) {
    size1 = size2 = size;
    super(size1, size2);
    this.size = size;
  }

  print () {
    super.print();
  }

  rotate () {
    super.rotate();
  }

  double () {
    super.double();
  }
}
module.exports = Square;
