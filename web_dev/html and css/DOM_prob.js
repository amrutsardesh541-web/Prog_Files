let h2 = document.querySelector("h2");
let old = h2.innerText;
console.log("OLD :",old);

old = old + " from Piyush Deshmukh";
console.log(old);

let allDivs = document.querySelectorAll(".box");
console.log(allDivs);
let galiya = ["Chu****", "Behen****", "Madar****"]
let idx = 0;
for(div of allDivs){
    //div.innerText = galiya[idx];
    idx++;
};