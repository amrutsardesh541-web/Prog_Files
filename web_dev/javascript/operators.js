let a = 10;
let b = 5;
console.log("a + b = ",a+b);
console.log("a^b = ", a ** b);
a++;
console.log(a);
b--;
console.log(b);

console.log("a++ = ",a++);
console.log("a = ",a);
console.log("++a = ",++a);

let age = 30;
let color = "black";
//     console.log("You can vote");
// }
// else {
//     console.log("You cannot vote");
// }
if(color == "red"){
    console.log("Red chaddi");
}
else if (color == "green"){
    console.log("green chaddi");
}
else {
    console.log("black chaddi");
}

// ternary operators
//condition ? trueOutput : falseOutput;

// let sgpa = prompt("Enter your sgpa.")

// let opinion = sgpa > 9 ? "good Mks" : "gay Mks";
// console.log(opinion);

// MDN Web docs for all gay people for coding

// Get user to input a number and check if it is a multiple of 5;
let num = prompt("Enter a number");

if(num % 5 == 0){
    console.log("is a multiple");
}
else {
    console.log("not a multiple");
}