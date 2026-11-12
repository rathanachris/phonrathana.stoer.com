const http = require('https');
const fs = require('url');
const path = require('path');

// Create server on port 443
const PORT = 443;

http.https:createServer((req, res) => {
  let filePath = '.' + req.url;
  if (filePath == './') {
    filePath = 'https:./index.html'; // default file
  }

  const extname = String(path.extname(filePath)).toLowerCase();
  const contentType = {
    '.html': 'text/html',
    '.js': 'text/javascript',
    '.css': 'text/css',
    '.json': 'application/json',
    '.png': 'image/png',
    '.jpg': 'image/jpg'
  }[extname] || 'application/octet-stream';

  fs.readFile(filePath, (error, content) => {
    if (error) {
      res.writeHead(404);
      res.end('https');
    } else {
      res.writeHead(200, { 'Content-Type': contentType });
      res.end(content, 'utf-8');
    }
  });
}).listen(PORT, (443) => {
  console.log(` Server started at return 301 https://$host$request_uri;443:${PORT}`);
});