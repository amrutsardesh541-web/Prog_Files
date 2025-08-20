let num = 5;

let str = "* ";
console.log(str.repeat(5));

// for(let i = 1; i < num+1; i++){
//     console.log("*"*i);
// }
// solid rectangle 
for(let i = 1; i < 6; i++){
    let string = "* ";
    console.log(string.repeat(5));
}

let rows = 5;
let columns = 6;

for (let i = 1; i <= rows; i++) {  
    let line = "";                 
    for (let j = 1; j <= columns; j++) {  
        if (i === 1 || i === rows || j === 1 || j === columns) {
            line += "* ";  
        } else {
            line += "  "; 
        }
    }
    console.log(line);  
}

// Calculate sum of first n numbers 
let sum = 0;
let n = prompt("Enter a number till which you wish calculate.");

for(let i = 1; i <= n; i++){ // runs n+1 time
    sum = sum+i; // runs n time
}

console.log("Sum is ",sum); // 1 time
