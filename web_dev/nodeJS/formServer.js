const http = require('http');
const fs = require('fs');
const querystring = require('querystring');

const server = http.createServer((req, res) => {
  if (req.method === 'GET' && req.url === '/') {
    
    fs.readFile('form.html', (err, data) => {
      if (err) {
        res.writeHead(500, {'Content-Type': 'text/plain'});
        res.end('Error loading form');
      } else {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.end(data);
      }
    });
  } 
  
  else if (req.method === 'POST' && req.url === '/submit') {
    let body = '';

    req.on('data', chunk => {
      body += chunk.toString();
    });

    req.on('end', () => {
      const parsedData = querystring.parse(body);

      const name = parsedData.name;
      const email = parsedData.email;
      const message = parsedData.message;

      const formData = `Name: ${name}\nEmail: ${email}\nMessage: ${message}\n\n`;

    
      fs.writeFile('form.txt', formData, (err) => {
        if (err) {
          res.writeHead(500, {'Content-Type': 'text/plain'});
          res.end('Error writing to file');
        } else {
          // After writing, read and show the content
          fs.readFile('form.txt', 'utf8', (err, data) => {
            if (err) {
              res.writeHead(500, {'Content-Type': 'text/plain'});
              res.end('Error reading the file');
            } else {
              res.writeHead(200, {'Content-Type': 'text/html'});
              res.end(`
                <h2>Thank you, ${name}! We have received your data.</h2>
                <h3>Form Data:</h3>
                <pre>${data}</pre>
              `);
            }
          });
        }
      });
    });
  } 
  
  else {
    res.writeHead(404, {'Content-Type': 'text/plain'});
    res.end('Page not found');
  }
});

server.listen(3000, () => {
  console.log('Server running at http://localhost:3000');
});
