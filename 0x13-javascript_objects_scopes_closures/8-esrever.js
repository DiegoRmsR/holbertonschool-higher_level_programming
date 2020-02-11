#!/usr/bin/node
/* function that returns the reversed version of a list */
exports.esrever = function (list) {
  const Mylist = [];
  for (let i = list.hength - 1; i >= 0; i--) {
    Mylist.push(list[i]);
  }
  return (Mylist);
};
