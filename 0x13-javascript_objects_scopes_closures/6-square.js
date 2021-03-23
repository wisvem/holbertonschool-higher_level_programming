#!/usr/bin/node
const Squares = require('./5-square');

class Square extends Squares {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    super.print(c);
  }
}

module.exports = Square;
