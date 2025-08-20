// strings are immutable.

let str = "Kya be bevde";
console.log(str.length);
for(let i = 0; i < str.length; i++){
    console.log(str[i]);
}

// template literals
let specialstr = `Yeh ek template literal hain` // special type of string
console.log(specialstr);

// template literals are equivalent to f-stings literals of python without f

let obj = {
    fullName : "Piyush Deshmukh",
    designation : "Chief minister"
};

console.log(obj.fullName,"is the",obj.designation,"of Maharashtra"); // yeh hain aam jindagi
console.log(`${obj.fullName} is the ${obj.designation} of Maharashtra`); // yeh hain mentos jindagi

// String interpolation upar dikhaya gaya which is nothing but filling the void swith placeholders

// escape charaters 
console.log("Akhil \nBhartiya \nVidyarthi \nParishad"); // ==> \n is escape character
console.log("Akhil \tBhartiya \tVidyarthi \tParishad"); // ==> \t is escape character
// \t or \n is considered a single character
// example
let s = "AB\nVP";
console.log(s.length); // is 5 and not 6

// string methods
let s1 = "Kutrya Bhokacha";
let s2 = " Gendu"
console.log(s1.toUpperCase());
console.log(s1.toLowerCase());
console.log(s1.trim());
console.log(s1.slice(0,7)); // slice(start,end) end not part of string
console.log(s1.concat(s2));
console.log(s1+s2);
console.log(s1.replace("Bhokacha", "Chutya")); // search text and repalcement
console.log(s1.charAt(3));

// Prompt the user to enter full name and generate a username for them starting with @ username and its length
let custName = prompt("Enter your name ");
console.log(`Your username is @${custName}${custName.length}`);


