#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w && h && h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const strng = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(strng.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
