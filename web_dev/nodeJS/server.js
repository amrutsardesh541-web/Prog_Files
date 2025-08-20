const http = require("http"); 
const fs = require("fs"); 
const path = require("path"); 
 
const server = http.createServer((req, res) => { 
  if (req.method === "GET" && req.url === "/") { 
    const filePath = path.join(__dirname, "index.html"); 
 
    fs.readFile(filePath, "utf8", (err, content) => { 
      if (err) { 
        res.writeHead(500, { "Content-Type": "text/plain" }); 
        res.end("Error reading index.html"); 
      } else { 
        res.writeHead(200, { "Content-Type": "text/html" }); 
        res.end(content); 
      } 
    }); 
  } else if (req.method === "POST" && req.url === "/submit") { 
    let body = ""; 
 
    req.on("data", (chunk) => { 
      body += chunk.toString(); 
    }); 
 
    req.on("end", () => { 
      try { 
        const data = JSON.parse(body); 
        console.log("Received inquiry:", data); 
 
        res.writeHead(200, { "Content-Type": "application/json" }); 
        res.end( 
          JSON.stringify({ 
            status: "success", 
            message: "Thank you for your inquiry!", 
          }) 
        ); 
      } catch (error) { 
        res.writeHead(400, { "Content-Type": "application/json" }); 
        res.end( 
          JSON.stringify({ status: "error", message: "Invalid data received" }) 
        ); 
      } 
    }); 
  } else { 
    res.writeHead(404, { "Content-Type": "text/plain" }); 
    res.end("Not found"); 
  } 
}); 
 
server.listen(3000, () => { 
  console.log("Server is running on http://localhost:3000"); 
});