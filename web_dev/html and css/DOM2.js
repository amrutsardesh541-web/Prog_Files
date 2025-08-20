let div = document.querySelector("div");
console.log(div);
let id_name = div.getAttribute("class");
console.log(id_name);

let body = document.querySelector("body");
// let colors = ["blue", "pink", "yellow", "red", "blue"];
// for (let i in colors) {
//     setTimeout(() => {
//         body.style.backgroundColor = colors[i];
//     }, i * 1000); // Change color every second
// }

// body.style.visibility = "hidden";

let newContent = document.createElement("p");
newContent.innerText = "Hello Ji How are Khana khake jana hann.";
body.append(newContent);

let body1 = document.querySelector("body"); // Select the body element
let Heading = document.createElement("h1"); // Create an h1 element
Heading.innerText = "HI"; // Set the text content of the h1
body1.prepend(Heading); // Prepend the h1 element to the body

let y = document.createElement("ul");
console.log(y);

y.innerText = "Y is y";
y.after(div);

// Node.append/.prepend/.before/.after(el);


