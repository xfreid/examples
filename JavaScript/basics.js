// the best practice to declare a variable is to use "let"
// if you don't initialize the variable, the variable value is "undefined"
// variable names can not contain "-"
// variable/function names are case sensitive
let name = 'Fei';
console.log(name);

// to delcare a constant, use "const"
// constant value can't change
const pi = 3.14;
// this will give "Assignment to constant variable" error
// pi = 2.4;

// there are two categories of data types
// primitives/value types
//    String
//    Number
//    Boolean
//    undefined
//    null
// reference types
//    Object
//    Array
//    Function

// Primitives
let str_lit = "string"; // String Literal
let num_lit = 30;       // Number Literal
let boo_lit = true;     // Boolean Literal
let to_clear = null;    // null is used to clear a variable value

// JavaScript is a dynamically typed language
let foo = 'foo'; // typeof returns "string"
// this is completely fine
foo = 2.4;   // typeof return "number"
console.log(foo);

// to declare an Object
let person = {
    // properties of person object
    // you dont' need to quote the property name, they will be 
    // treated as strings
    name: 'Fei',
    age: 45
};
console.log(person);

// use dot notation to access object properties
person.name = 'John';
console.log(person.name);

// use bracket notation
person['name'] = 'Mary';
console.log(person['name']);

// if the property (name) contains space, you would have to
// quote it, and you have to use bracket notation
let person2 = {
    "first name": "John",
    "last name": "Wick"
}
console.log("person2's first name is " + person2['first name']);

// you can add properties to an object using dot or bracket notation
console.log('after adding properties to person2');
person2.age = 34;
person2['work phone'] = '2023034056';
console.log(person2);

// to delete properties, use "delete" keyword
delete person2.age
console.log('after deleting person2 age');
console.log(person2);

// to check if a property exists
if (person2.hasOwnProperty('work phone')) {
    console.log('person2 has work phone number' + person2["work phone"]);
}

// to declare an Array
let selectedColors = ['red', 'blue'];
// to declare an empty Array
// let emptyArray = [];
console.log(selectedColors);

// to access individual element in the Array
selectedColors[0] = 'yellow';
console.log(selectedColors[0]);

// size of the Array is dynamic (i.e. not fixed)
selectedColors[2] = 'green';
console.log(selectedColors);

// type of each element can be different
selectedColors[3] = 1;
console.log(selectedColors);

// Array is also an Object, it has some built-in properties
console.log(selectedColors.length);

// to declare a function
function greet() {
    console.log('Hello');
}
greet();

// function with parameters
function greet2(name) {
    console.log('Hello ' + name);
}
greet2('John');

// what happens if you just call greet2()
// in this case, name would be undefined

// function returns a value
function square(number) {
    return number * number;
}
let number = square(5);
console.log(number);
// or simply
console.log(square(5));

// Learn JavaScript - Full Course for Beginners
// https://www.youtube.com/watch?v=PkZNo7MFNFg

/* this is a 
   multi-line
   comment
*/
// end ending ; is not required, but recommended
let no_semi = 'this is fine'

// math operations
let numSum = 10 + 2;
console.log(numSum);
/*
 similarly, 
    - for subtraction
    * for multiplicaiton
    / for division
    % for remainder
    ++ for increment
    -- for decrement
 example,
 5 - 3
 2.0 * 1.3
 1.5 / 0.2

 a = a + 5 is same as a += 5
 b = b - 2 is same as b -= 2
 c = c * 3 is same as c *= 3
 ...
*/

// more math
console.log('More math operations');
console.log(Math.sqrt(2));
console.log(Math.pow(4, 3));
console.log(Math.round(3.4));


// to escape a double quote
let has_quotes = "this is a sting that contains \"double quotes\"";
// or
let has_quotes_2 = 'this is a string that contains "double quotes"';
// or
let has_quotes_3 = `this is a string that contains 'single quotes' and "double quotes"`;

// to concatenate two strings
let combined = "string 1 " + "string 2";
console.log(combined);

let combined_2 = 'string 1 ';
combined_2 += 'string 2 ';

let string_3 = 'string 3';
combined_2 += string_3
console.log(combined_2);

// string is like an Array
// to get string length
console.log("combined string has length of " + combined.length);

// to get sub-string using bracket notation
console.log("the second letter of combined string is " + combined[1]);

// to get the last letter of the string
console.log("the last letter of combined string is " + combined[combined.length - 1]);


// strings are immutable
// this will not change the first letter of the string 
// Cannot assign to read only property '0
// combined[0] = "T";
// combined still remains as "string 1 string 2"
console.log(combined);
// to change a string variable, you would have to assign the variable to another string
combined = "this will work";
console.log(combined);

// nested Array
let nested_array = [
    ["John", 23], 
    ["Mary", 30] 
];
console.log("John has age of " + nested_array[0][1]);

// to append to an Array
let my_array = ['John', 'has'];
my_array.push('dog')
my_array.push(['and', 'cat']);
// my_array equals "[ 'John', 'has', 'dog', [ 'and', 'cat' ] ]"
console.log(my_array);

// pop() removes the last element of the Array
let removed = my_array.pop()
// removed equals "[ 'and', 'cat' ]"
console.log(removed);
// my_array now equals "[ 'John', 'has', 'dog' ]"
console.log(my_array);

// shift() removes the first element of the Array
removed = my_array.shift();
// removed equals "John"
console.log(removed);
// my_array now equals "[ 'has', 'dog' ]"
console.log(my_array);

// unshift() prepend to the Array
my_array.unshift(removed)
// my_array now equals "[ 'John', 'has', 'dog' ]"
console.log(my_array);

// scope
// variable defined outside funciton has global scope
// it can be used anywhere in the program
var myGlobal = 10;

function varInFunction() {
    // variable declared in a function with "var" has local scope (scoped to function)
    var localVar = 20;
}

function testGlobal() {
    if (typeof myGlobal != 'undefined') {
        console.log('myGlobal has value of ' + myGlobal);
    }

    if (typeof lovalVar == 'undefined') {
        console.log('we can not access localVar');
    }
}
testGlobal();

// if statement
if (true) {
    console.log('this is true');
} else {
    console.log('this is false');
}

// comparison
// similarly "!=" for inequality
let numberToCompare = 10;
if (numberToCompare == 10) {
    console.log('number equals 10');
}

// strict equal sign "==="
// similarly "!==" for strict ineqaulity
let three = 3;
if (three == '3') {
    // this condition is hit because "==" will convert the operands to a common type
    // in this case, it converts string '3' to a number
    console.log('three equals 3');
}
// strict equality operator "===" checks the data type
// number is NOT same as string
if (three === '3') {
    console.log('three equals to 3');
} else {
    // this condition is hit
    console.log('three is not equal to 3');
}

// other operator
// >, <, >=, <=
// &&, ||, 
if (numberToCompare > 5 && numberToCompare < 15) {
    console.log('number is greater than 5 and less than 15');
}

// else if
if (numberToCompare < 5) {
    console.log('number is less than 5');
} else if (numberToCompare > 15) {
    console.log('number is greater than 15');
} else {
    console.log('number is between 5 and 15');
}

// switch statement
switch(numberToCompare) {
    case 1:
        console.log('number is 1');
        break;
    case 2:
        console.log('number is 2');
        break;
    default:
        console.log('number is neither 1 nor 2');
        break;
}

// switch works for string too
let selector = "c";
switch (selector) {
    case "a":
        console.log('apple');
        break;
    case "b":
        console.log('banana');
        break;
    default:
        console.log('cat');
        break;
}

// multiple conditions
switch(numberToCompare) {
    case 1:
    case 2:
    case 3:
        console.log('number is 1, 2 or 3');
        break;
    case 4:
    case 5:
        console.log('number is 4 or 5');
        break;
    // it is fine to have mixed types
    case "something":
        console.log('some string');
        break;
    default:
        console.log('number is other');
        break;
}

// complex object
// example, array of objects
let myMusic = [
    {
        "artist": "Michael Jackson",
        "title": "Walking on Moon",
        "formats" : ["CD", "DVD", "MP3"],
        "award": true    
    },
    {
        "artist": "Mariah Carey",
        "title": "Hero",
        "formats" : ["CD", "DVD", "Youtube"],
        "award": false    
    }
];
console.log('My second artist is ' + myMusic[1].artist)

// another example
let myBooks = {
    "book1" : {
        "author" : {
            "first name" : "John",
            "last name" : "Foo"
        },
        "info" : {
            "price" : 40,
            "bought ag": "Amazon"
        }
    },
    "book2" : {
        "author" : {
            "first name" : "Mary",
            "last name" : "Bar"
        },
        "info" : {
            "price" : 25,
            "bought at": "Local Store"
        }
    }
};
console.log('My second book is bought with ' + myBooks.book2.info.price);

// while loop
let i = 0;
let loopArray = [];
while (i < 5) {
    loopArray.push(i);
    i++;
}
console.log(loopArray);

// for loop
for (let i = 0; i < 5; i++) {
    loopArray.push(i);
}
console.log(loopArray);

// iterate through an Array
let totalInArray = 0;
for (let i = 0; i < loopArray.length; i++) {
    totalInArray += loopArray[i];
}
console.log('the total of loopArray is ' + totalInArray);

// do...while loop
let j = 6;
let loopArray2 = [];
// do at least once before checking the condition
do {
    loopArray2.push(j);
    i++;
} while (i < 5)
console.log(loopArray2);

// random number generation
// Math.random generate a number between 0 and 1 
// [0, 1)
let randomNum = Math.random();
console.log(randomNum);

// to generate a random whole number between 0 and 20
let randomNum2 = Math.floor(Math.random() * 20);
console.log(randomNum2);

// to genreate a random whole number in a range
let min = 10;
let max = 20;
let randomNum3 = Math.floor(Math.random() * (max - min + 1)) + min;
console.log(randomNum3);

// parseInt function
// takes a string and return an integer
console.log(parseInt("56"));
// it can handle number with different base (radix)
console.log(parseInt("10010", 2));

// conditional ternary operator
let isEqual = 10 === min ? true : false;
console.log(isEqual);

// nested conditional ternary expression
let sign = min > 0 ? "postive" : min < 0 ? "negaive" : "zero";
console.log(sign);

// const Array
// if an Array is declared as const, you can NOT re-assign the Array
// but you can mutate the Array with bracket notation
const constArray = [1, 2, 3];
// this will give "Assignment to constant variable" error
// constArray = [4, 5, 6]
constArray[0] = 4; 
console.log(constArray);

// similarly, if an Object is eclared as const, you can
// still mutate the proeprties in Object using dot/bracket noation
const MATH_CONST = {
    "PI" : 3.14
}
MATH_CONST.PI = "surprise";
console.log(MATH_CONST);

// with Object.freeze
Object.freeze(MATH_CONST);
MATH_CONST.PI = "second try";
// MATH_CONST ramins as "{ PI: 'surprise' }"
console.log(MATH_CONST);

// anonymous function
let magic = function() {
    return new Date();
};
console.log(magic());

// this can be simplied using Arrow function 
let magic2 = () => { return new Data() };
// or even
let magic3 = () => new Date();
console.log(magic3());

// Arrow function with parameters
let myConcat = function(arr1, arr2) {
    return arr1.concat(arr2);
};
console.log(myConcat([1, 2], [3, 4, 5]));

// if there is only one parameter, you can skip the ( )
// param => { statements };
let myConcat2 = (arr1, arr2) => arr1.concat(arr2);
console.log(myConcat2([1, 2], [3, 4, 5]));

// 
const realNumArray = [1.2, 3, -9.8, 0, 5.6, -2.1, 6, -8, 9]
const squareList = (arr) => {
    // filter() takes a function as argument
    const squaredInteger = arr.filter(num => Number.isInteger(num) && num > 0).map(x => x * x);
    return squaredInteger;
}
console.log(squareList(realNumArray));

// return a function
// in this example, anonymous function returns a normal function 
// function () {...} is anonymous function
// (funtion () {...}) () basically calls this anonymous function
// which returns function _increment
const increment = (function () {
    // "value" parameter has default value of 1 
    return function _increment (number, value = 1) {
        return number + value;
    }
}) ();
// return 5 + 2
console.log(increment(5, 2));
// return 5 + 1
console.log(increment(5));

// the following code does the equivalent
function _increment2(number, value = 1) {
    return number + value;
}
const increment2 = _increment2;
console.log(increment2(5));

// rest operator "..." can take a various number of arguments
// ... converts all the arguments into an Array
function sum (...args) {
    // adds all the elements in the Array args
    return args.reduce((a, b) => a + b, 0)
}
console.log(sum(1, 2, 3, 4, 5));

// By default, JavaScript is assign by reference, not by value
let myArr1 = ['foo', 'bar', 'xyz']
let myArr2 = myArr1;
myArr1[0] = 'Hello';
// what ever you changed in myArr1 is reflected in myArr2 too
console.log(myArr2[0]);

// Spread operator spreads the content of an Array
// we use this operator to achieve assign by value
let myArr3 = [...myArr1];
myArr1[0] = 'World';
// myArr3[0] remains "Hello"
console.log(myArr3[0]);

// destructing assignment
// old way of assigning each property of the Object to a variable
let myObj = {x: 3.6, y: 4.1, z: 5.4};
let a1 = myObj.x;
let b1 = myObj.y;
let c1 = myObj.z;

// new way of using destruction assginment
const {x: a2, y: b2, z: c2} = myObj;
console.log(a2 + " " + b2 + " " + c2);

// you don't need to get all the properties, subset is fine
const {y: b3} = myObj;
console.log(b3);

// destructing assignment for nested Object
const FORCAST = {
    today: {
        min: 72,
        max: 83
    },
    tomorrow: {
        min: 73.3,
        max: 84.6
    }
};
const {tomorrow: { max: tomorrow_max }} = FORCAST;
console.log(tomorrow_max);

// destructing assignment works for Array too
const [first, second] = realNumArray;
// first gets 1.2, seconds gets 3
console.log('first is ' + first + ' second is ' + second);

// if you want a number somewhere in between, for example
// the fourth numberin realNumArray
const [, , , fourth, , sixth] = realNumArray;
// fourth gets 0, sixth gets -2.1
console.log('fourth is ' + fourth + ' sixth is ' + sixth);
// or
console.log(fourth, sixth);

// to switch two variable values
let varFoo = 'Foo';
let varBar = 'Bar';
[varBar, varFoo] = [varFoo, varBar];
console.log(varFoo, varBar);

// use destructing assignment with rest operator
// example, remove the first two elements of the source Array
// and assign to the dest Array
sourceArray = [1, 2, 3, 4, 5, 6];
const [, , ...destArray] = sourceArray;
console.log(destArray);

// use destructing assignment to pass an Object as function's parameter
let stats = {
    min: -0.75,
    max: 86.75,
    median: 23.7,
    average: 35.8,
    mode: 29
}

// if a function only needs a couple of properties of stats Object
// you don't have to pass the whole stats as a parameter
// in the following example, only stats.max and states.min are used
// by the function
function half ({max, min}) {
    return (max + min) / 2;
}
console.log(half(stats));

// template literal
// it is useful to 
// 1. create multi-line string
// 2. have double or single quotes in the string without escaping
// 3. put variables directly in string
const greeting = `Hello, my name is ${person.name}!
I am ${person.age} years old.`;
console.log(greeting);

// a concise way to create an Object
// supose we need to create Object with following properties
// name: name
// age: age
// gener : gender
const createPerson = (name, age, gender) => {
    return {
        // property name matches the propery value variable name
        name: name,
        age: age,
        gender: gender
    };
};
// we can simplify this to
const createPerson2 = (name, age, gender) => ( {name, age, gender} );
console.log(createPerson2('John', 34, 'male'));

// you can define a function in Object
const bicycle = {
    gear : 2,
    setGear : function(newGear) {
        this.gear = newGear;
    }
};
bicycle.setGear(3);
console.log(bicycle.gear);

// it can be written as
const bicycle2 = {
    gear : 2,
    setGear(newGear) {
        this.gear = newGear;
    }
};
bicycle2.setGear(4);
console.log(bicycle2.gear);

// class
class SpaceShuttle {
    constructor(targetPlanet) {
        this.targetPlanet = targetPlanet;
    }
}
// this is equivalent to
// let planet = {
//    targetPlanet: "Jupiter"
// };
let planet = new SpaceShuttle('Jupiter');
console.log(planet.targetPlanet);

// you can return a class from a function
function createClass() {
    class Vegetable {
        constructor(name) {
            this.name = name;
        }
    }
    return Vegetable;
}

let VegClass = createClass();
let carrot = new VegClass('my carrot');
console.log(carrot.name);

// getter and setter for class object
class Book {
    // _author is private, you don't want 
    // to expose it to the client, client
    // should use getter and setter
    constructor(author) {
        this._author = author;
    }
    // getter
    get writer() {
        return this._author;
    }
    // setter
    set writer(newAuthor) {
        this._author = newAuthor;
    }
}

const myBook = new Book('John Wick'); 
// access the getter and setter as if they are property
// do NOT put () at the end
let bookAuthor = myBook.writer;
myBook.writer = "John Hawk";
bookAuthor = myBook.writer;
console.log(bookAuthor);
console.log(myBook._author);

// import functions from other files
// .js extension is not required
import { capitalizeStr } from "./string_func.js";
// console.log(capitalizeStr('hello'));

// if you want to import everything
// impot * as mymodule from './string_func.js';

// export default

// import default
