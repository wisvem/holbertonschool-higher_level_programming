#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const result = list.filter(function (element) {
    return element === searchElement;
  });
  return result.length;
};
