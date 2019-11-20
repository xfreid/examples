// Hello World
var msg = 'Hello World';
console.log(msg);

// Node JS Tutorial for Beginners
// https://www.youtube.com/playlist?list=PL4cUxeGkcC9gcy9lrvMJ75z9maRw4byYp

// -----------------------------------------------
// global objet
// -----------------------------------------------
// in browser, the global object is "window"
// global object can be accessed anywhere
// console is short for window.console
// however, in node, we don't have "window" object, instad we have "global"
// so console in node is short for global.console

// similarly, setTimeout is equivalent to global.setTimeout
// setTimeout() calls a function after a certain amount of time
// setInternal() repeatedly calls a function after a acertain delay
// note setTimeout and setInterval are not blocking
setTimeout(function() {
    console.log("3 seconds have passed")
}, 3000);

var time = 0;
var interval = setInterval(function() {
    time += 2; 
    console.log(time + " seconds have passed")
    if (time > 5) {
        clearInterval(interval);
    }
}, 2000);

// more global object
// the directory where the file is in 
console.log("dirname is " + __dirname);
// full path to the current file
console.log("filename is " + __filename);

// define a variable
var message = ''
// variable in node is not in global scope, it is in the file scope
// so you can't use global.message

// -----------------------------------------------
// function expression
// -----------------------------------------------

// normal function statement
function sayHi() {
    console.log("Hi");
}
sayHi();

// function expression
// we assign an anonymous function to a variable
var sayBye = function() {
    console.log("Bye");
};
sayBye();

// we can pass a function expression to a function
function callFunc(fun) {
    fun();
}
callFunc(sayBye);

// -----------------------------------------------
// module
// -----------------------------------------------

// we don't typically write all the code in one file
// to import a module
// requrie() returns the exported funciton
var counter = require('./count');  // no .js is needed
console.log(counter(['karen', 'Shawn', 'Rye']));


