// Dom Manipulation


let from_id = document.getElementById("heading");
console.dir(from_id);

let from_class = document.getElementsByClassName("para")
console.dir(from_class);

// let firstElements = document.querySelector(className, idName, tagName) // returns firstElemtent
// let allElements = document.querySelectorAll(className, idName, tagName) // returns all the elements

let firstElements = document.querySelector("p"); // returns firstElemtent
console.log(firstElements);
let allElements = document.querySelectorAll("p");
console.log(allElements);

let firstElementClass = document.querySelector("#heading");
console.log(firstElementClass);

// DOM Properties
// Tagname
let getTagName = firstElements.tagName;
console.log(getTagName);

// getHTML
let x = document.querySelector("#body-class"); // returns firstElemtent
console.log(x);
let getHTML = x.innerHTML;
console.log(getHTML)

// getText
let getText = x.innerText;
console.log(getText);

// get first child
// types of nodes in DOM tree => 1. text nodes, comment nodes, element nodes
console.log(x.children);