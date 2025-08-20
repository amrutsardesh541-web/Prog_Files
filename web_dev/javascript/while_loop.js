// let i = 0;

// // while loop
// while (i <= 5){
//     console.log(i);
//     i++;
// }

// // do while
// // Bismillah game
// let j = 10;
// do {
//     console.log(j);
//     j--;
// } while(j >= 0);

// console.log("Bismillah \n Boom \n boom")



// // for of loop
// for(letVal of strVar){
//     // do work
// }

// for of loop ==> for strings and arrays
let str = "Lavdya abhyas Kar";
let size = 0;
for(let val of str){
    // console.log(val);
    size++;
}

console.log("Length of the string ",str," is ",size);

// for in loop ==> for objects

let college = {
    collegeName : "Sant Haridas Institute of Technology, Gadchiroli (SHIT)",
    department : 5,
    ranking : "NAAC Z++"
};

for(key in college){
    console.log(key," : ",college[key]);
}

// print all the even numbers
console.log("print all the even numbers from 0 to 100")
for(let i = 0; i <= 100; i++){
    if(i%2 === 0){
        // console.log(i);
    }
    else {
        continue;
    }
}

// create a random game guessing number
let randNum = 123;
let guess = 5;
for(let i = 1; i <= guess; i++){
    let guessNum = parseInt(prompt("Enter your guess"));
    if(guessNum === randNum){
        console.log("Jabardast");
    }
    else {
        guess--;
        console.log("Chutiya banaya. Guess remaining ",guess);
    }
}