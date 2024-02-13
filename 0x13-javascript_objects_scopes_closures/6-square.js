#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.width; i++) { console.log(c.repeat(this.width)); }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
