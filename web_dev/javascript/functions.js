function Message(name){
    console.log("Hello",name);
}

Message("Piyush");

function add(n1,n2){
    return n1+n2;
}
let s = add(2,3);
console.log(s);

// Params are having block scope till function
// arrow functions in Modern js
const mul = (a,b) => {
    console.log(a*b);
}

mul(5,10);

// Function to return number of vowels
let vowcnt = 0;
function Vowel(str){
    for(let i = 0; i < str.length; i++){
        if(str[i] === "a" || str[i] === "e" || str[i] === "i" || str[i] === "o" || str[i] === "u"){
            vowcnt++
        }
    }
    console.log(vowcnt);
}

Vowel("Piyush");

let vowcnt1 = 0;
const arrVow = (str) => {
    for(let i = 0; i < str.length; i++){
        if(str[i] === "a" || str[i] === "e" || str[i] === "i" || str[i] === "o" || str[i] === "u"){
            vowcnt1++
        }
    }
    console.log(vowcnt1);
}

arrVow("Prasanna");

// for each is a higher order func to loop in arrays
// a func which may have a function itself as a parameter is a high order function
arr1 = [1,2,3,4];

let calCub = (num) => {
    //console.log(num**3);
    return num**3;
}

arr1.forEach(calCub); // function la adhich o/p print karava lagta

// map method => navin array bante after some operation

let new_arr1 = arr1.map(calCub); // function la o/p fakt return karava lagta
console.log(new_arr1);

let inverseArr = arr1.map((val) => {
    return val**-1
})
console.log(inverseArr);

// filter method => existing array madhle je element condn la satisfy kartat tyanchi array

let evenArr = arr1.filter((val) => {
    return val%2 === 0;
})
console.log(evenArr);

// reduce => samja purna array chya saglya elements var ekatra konta pn operation karaycha asel tar
let sumOf = arr1.reduce((result, element) => {
    return result + element;
})
console.log(sumOf);

let max = arr1.reduce((res, curr)=> {
    return res > curr ? res : curr;
})
console.log(max);

// Ques.1
let arr2 = [67,89,90,98,95,79,91,90];
let toppers = arr2.filter((val) => {
    return val >= 90;
})
console.log("Topper mks are", toppers);

// Ques.2
let a = parseInt(prompt("Enter a number"));
let arr3 = [];
for(let i = 1; i <= a; i++){
    arr3.push(i);
}
console.log(arr3);

let SUM = arr3.reduce((res, curr) => {
    return res+curr;
})
console.log(SUM);

let PROD = arr3.reduce((res, curr) => {
    return res*curr;
})
console.log(PROD);
