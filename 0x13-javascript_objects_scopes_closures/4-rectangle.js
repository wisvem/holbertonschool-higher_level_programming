#!/usr/bin/node
class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print (c) {
    if (c === undefined) c = 'X';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }

  rotate () {
    this.height = this.width + this.height;
    this.width = this.height - this.width;
    this.height = this.height - this.width;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
