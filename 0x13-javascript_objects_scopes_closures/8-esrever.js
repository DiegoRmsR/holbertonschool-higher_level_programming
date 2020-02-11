#!/usr/bin/node
/* function that returns the reversed version of a list */
exports.esrever = function (list) {
  const new_list = [];
  for (let i = list.length - 1; i >= 0; i--) {
    new_list.push(list[i]);
  }
  return (new_list);
};
