/*
 * script.js
 * Copyright (C) 2016-04-19 17:10 coconor <coconor@umich.edu>
 *
 */
function processData(input) {
    //Enter your code here
    console.log(input);
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
