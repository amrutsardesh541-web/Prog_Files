// arrays

let mks = [12,13,20,14,9];

// for(let i = 0; i < mks.length; i++){
//     console.log(mks[i]);
// }

let heroes = ["ironman", "hulk", "spiderman"];

for(let i = 0; i < heroes.length; i++){
    console.log(heroes[i]);
}

console.log(typeof(heroes)); // object

// let arr = [];
// let size = prompt("Enter the size of array");
// for(let j = 0; j <= size-1; j++){
//     let num = prompt("Enter your number");
//     arr[j] = num;
// }

// console.log(arr);

// For a given array of marks of students find the avg of entire class
let stu = [85,97,44,37,76,60];
let sum = 0;
for(let k = 0; k < stu.length; k++){
    sum += stu[k];
}

let avg = sum/stu.length;
console.log(avg);

// methods in array
// 1. push similar to stack

let a1 = [1,2,3];
console.log(a1);
a1.push(4);
console.log(a1);
console.log(a1.pop());
console.log(a1.toString());
arr1 = [4,5,6];
arrCon = a1.concat(arr1);
console.log(arrCon);
arrCon.unshift(0);
console.log(arrCon);
let delItem = arrCon.shift();
console.log(delItem);
console.log(arrCon.slice(0,3));
arrCon.splice(2, 2, 101, 102);
console.log(arrCon);
// push is element added at last and unshift is at first
// pop is element delete at last and shift is at first


// let a3 = [250,645,300,900,50];
// console.log(a3);
// // dp = mrp - (mrp*percentage in decimal)
// for(let l = 0; l < a3.length; l++){
//     let dp = a3[l] - (a3[l]*0.1);
//     a3[l] = dp;
// }
// console.log(a3);


