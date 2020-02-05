#!/usr/bin/node
/*
 * script that computes and prints a factorial
 */
function factorial (num) {
  if ((Number.isNaN(num)) || (num === 1)) {
    return 1;
  }
  return factorial(num - 1) * num;
}
const num = parseInt(process.argv[2]);
console.log(factorial(num));
