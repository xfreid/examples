// this is a module
// module is another .js file
var counter = function(arr) {
    return "there are " + arr.length + " elements in this array";
};

// console.log(counter(['karen', 'Shawn', 'Rye']));

// to explicitly declare what to export
module.exports = counter; 