// primitives: numbers, strings, booleans (true/false)
//cannot be changed, we turn 5 into 6 by making a 6 and throwing the 5 away

//objects: immutable and can be changed
//functions = function() {}
//objects = {}
//arrays = []

// primitives: immutable - stack
// objects: mutable - heap

//const x gets hello
const x = 'hello';
const i = 0;

const school = 123;
console.log(typeof(school.toString())); //6
//console.log(typeof(school))

// LHR (left hand reference)
let j = 0;
j++;

//let replaces var, but we default to const unless we know something's mutable

const nums = [];
nums.push(5);
//console.log(nums);
