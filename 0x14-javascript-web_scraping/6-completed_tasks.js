#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const newdict = {};
    const jsonb = JSON.parse(body);
    for (let i = 0; i < jsonb.length; i++) {
      if (jsonb[i].completed === true) {
        if (jsonb[i].userId in newdict) {
          newdict[jsonb[i].userId] += 1;
        } else {
          newdict[jsonb[i].userId] = 0;
        }
      }
    }
    console.log(newdict);
  }
});
