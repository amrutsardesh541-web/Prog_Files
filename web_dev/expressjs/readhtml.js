const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();

app.use(express.static('public'));

app.get('/', (req,res) => {
    // const filePath = path.join(__dirname, 'public', 'index.html');
    fs.readFile('index.html', 'utf-8', (err,html)=>{
        if(err){
            console.error("Error reading");
            return res.status(500).send('Server Error');
        }
        else {
            res.send(html);
        }
    });
});

app.listen(3000, ()=>{
    console.log("Server running at http://localhost:3000");
})