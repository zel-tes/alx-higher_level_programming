#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w && h && h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
