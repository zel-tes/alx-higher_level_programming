#!/usr/bin/node
const Square = require('./5-square');
class Square1 extends Square {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      const strng = c;
      for (let i = 0; i < this.size; i++) {
        console.log(strng.repeat(this.size));
      }
    }
  }
}
module.exports = Square1;
