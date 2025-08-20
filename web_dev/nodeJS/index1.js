// console.log("Hello world");

const fs = require('fs');
const http = require('http');

fs.appendFile('test2.txt', '\n Mujhe add kiya gaya hain', (err)=>{
    if(err) throw err;

    console.log("We have appended the file");
    
})