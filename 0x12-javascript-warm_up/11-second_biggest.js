#!/usr/bin/node
/*
 * script that searches the second biggest
 * integer in the list of arguments.
*/
let arg = 0;
let num = 0;
let num1 = 0;
let num2 = 0;

arg = process.argv.length;

if (arg <= 2 || arg === 3) {
  console.log(0);
} else {
  for (let i = 2; i < arg; i++) {
    num = parseInt(process.argv[i]);
    if (num > num1) {
      num2 = num1;
      num1 = process.argv[i];
    } else if (num > num2 && num !== num1) {
      num2 = num;
    }
  }
  console.log(num2);
}
