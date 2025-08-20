let btn = document.getElementById('btn');
let content = document.querySelector('.sec');
console.log(btn.innerHTML);
console.log(content.innerHTML);

addEventListener('click', function(){
    content.innerHTML += "<p>Why you touch</p>";
});

addEventListener('dblclick', function(){
    document.body.style.backgroundColor = "red";
});

addEventListener('mouseover', function(){
    content.innerHTML += "<h1>Haath hata bhadwe</h1>";
});