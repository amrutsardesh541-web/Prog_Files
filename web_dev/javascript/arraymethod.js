// An array is a variable which is used to store multiple values 
// in common practice it is declared using a const variable 
// the elements in the array has an index starting from 0 to n 

// let array = [1,2,3,4];
// console.log(array);

// Array methods
let arr = [1,2,3];
arr.push(4);
console.log(arr);

arr.pop()
console.log(arr);

arr.unshift(0);
console.log(arr);

arr.shift();
console.log(arr);

let l = arr.length;
console.log(l);

arr.forEach(function(item,index){
    console.log(item+" : "+index);
});

let arr2 = [1,2,3,4,5,6,7,8]
arr2.splice(1,4,'a','b','c','d'); // start idx, end idx, new value 
console.log(arr2);

let arr3 = arr2.slice(2,5);
console.log(arr3);