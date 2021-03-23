#!/usr/bin/node
exports.converter = function (base) {
  return function myConv (num) {
    return num.toString(base);
  };
}
;
