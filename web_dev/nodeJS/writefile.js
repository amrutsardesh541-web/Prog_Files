const fs = require('fs');

fs.writeFile('test2.txt', 'I was written using [fs] module of node.js', (err) =>{
    if(err){
        console.log("Error writing a file");
    }
    else {
        console.log("Successful in writing");
    }
});