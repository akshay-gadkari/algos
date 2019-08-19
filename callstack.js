// call stack is the stack of all functions in the code
// program is a function with frames (smaller functions) nested inside 
// when a new function is invoked, a new frame is added to the call stack
// stack trace - when you get an error, stack trace helps you find where the error might be (console.trace)

//console.trace();

// Error: some error
//     at Object.<anonymous> (/home/mipham/LambdaSchool/algos/callstack.js:8:7)     //where the function is run
//     at Module._compile (internal/modules/cjs/loader.js:701:30)      //where the function is compiled?
//     at Object.Module._extensions..js (internal/modules/cjs/loader.js:712:10)
//     at Module.load (internal/modules/cjs/loader.js:600:32)
//     at tryModuleLoad (internal/modules/cjs/loader.js:539:12)
//     at Function.Module._load (internal/modules/cjs/loader.js:531:3)
//     at Function.Module.runMain (internal/modules/cjs/loader.js:754:12)
//     at startup (internal/bootstrap/node.js:283:19)
//     at bootstrapNodeJSCore (internal/bootstrap/node.js:622:3)

// manually created an error
//throw new Error('my error message');

function a() {
    console.trace();
}

function b() {
    a();
}

function c() {
    b();
}

c();


// primitive data types eg strings, numbers, booleans (true/false)
// objects in JS - everything that's not a primitive: arrays [], objects {} like hash tables, functions, maps, sets 

// primitives live on the stack, objects are on the heap
// primitives are all immutable, you can't change a string into another string, but you can delete a string and replace it (what all string methods do)

// 'char at' is a method that can be used on any string

