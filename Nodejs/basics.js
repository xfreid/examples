// Hello World
// var keyword is not "required"
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
// requrie() returns the exported function
var counter = require('./count');  // no .js extension is needed
console.log(counter(['karen', 'Shawn', 'Rye']));


// ---------------------------------------------------------------------
// first class function
// https://www.youtube.com/watch?v=kr0mpwqttM0 
// ---------------------------------------------------------------------
function square(x) {
    return x * x
}

// f gets the result of the function call
f1 = square(5)
// this prints something like "[Function: square]"
console.log(square)
console.log(f1)

// however, you can assign the function itself to a variable
// f2 is like function pointer in C++
f2 = square

//  f2 can now be used exactly as square
console.log(f2(5))

//pass a function as argument to another function
function my_map (func, arg_list) {
    result = []
    for (var i = 0; i <= arg_list.length; i++) {
        result.push(func(i))
    }
    return result
}

// you can replace "square" with "f2"
var squares = my_map(square, [1, 2, 3, 4, 5])
console.log(squares)

function cube(x) {
    return x * x * x
}

var cubes = my_map(cube, [1, 2, 3, 4, 5])
console.log(cubes)

// return a function from a function
function logger(msg) {
    function log_message() {
        console.log('Log:', msg)
    }
    return log_message
}

var log_hi = logger('Hi!')
log_hi()

// a slightly complex example
function html_tag(tag) {
    function wrap_text(msg) {
        console.log('<' + tag + '>' + msg + '</' + tag + '>')
    }
    return wrap_text
}

var print_h1 = html_tag('h1')
// this prints something like "[Function: wrap_text]"
// console.log(print_h1)
print_h1('Test Headline!')
print_h1('Another Headline!')

var print_p = html_tag('p')
print_p('Test Paragraph')


