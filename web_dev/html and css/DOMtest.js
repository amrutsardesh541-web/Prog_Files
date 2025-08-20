function aankh() {
    document.getElementById("message").innerHTML += "Aankh dikhata hai";
}

function ekdaclick() {
    document.getElementById("message").innerHTML += "Click kyun kiya";
}

function punhaclick() {
    document.getElementById("message").innerHTML += "Phir se click kyun kiya";
}

function baher() {
    document.getElementById("message").innerHTML += "Ab kyun dar gaya";
}

let x = document.getElementById("btn"); 
x.addEventListener("mouseover", aankh);
x.addEventListener("click", ekdaclick);
x.addEventListener("dblclick", punhaclick);
x.addEventListener("mouseout", baher);
