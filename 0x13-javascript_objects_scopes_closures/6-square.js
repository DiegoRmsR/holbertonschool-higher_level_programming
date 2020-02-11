#!/usr/bin/node
/* class Square that defines a square and
   inherits from Square of 5-square.jsn */
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let count = 0; count < this.width; count++) {
      console.log(c.repeat(this.height));
    }
  }
};
