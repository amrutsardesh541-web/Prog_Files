const http = require('http');

const server = http.createServer((req,res)=>{
    res.writeHead(200, {'Content-Type':'text/plain'});
    res.write('Node.js chya server madhe swagat aahe');
    res.end();
})

server.listen(1000, ()=>{
    console.log("Server is running on http://localhost:1000");
})