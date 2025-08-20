const fs = require('fs');

fs.readFile('test2.txt', 'utf-8', (err,data)=>{
    if(err){
        console.log("Error");
    }
    else {
        console.log("File Content");
        console.log(data);
    }
})