var express = require('express');
var path = require('path');
var app = express();

// Serve static files from "public" folder
app.use(express.static('public'));

app.get('/hello', function(req, res) {
    res.send('Hello World');
});

app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});


app.get('/about', function(req, res) {
    res.sendFile(path.join(__dirname, 'public', 'about.html'));
});

app.get('/contact', function(req, res) {
    res.sendFile(path.join(__dirname, 'public', 'contact.html'));
});

app.listen(3000, function() {
    console.log('Server is running on http://localhost:3000');
});
