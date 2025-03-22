# EX01 Developing a Simple Webserver
## Date:22-03-2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<title>Top Indian Companies</title>
<body>
<table border="2" cellspacing="10" cellpadding="6">
<caption>Top 5 Revenue Generating Indian Companies</caption>
<tr>
<th>s.no</th>
<th>companies</th>
<th>revenue</th>
</tr>
<tr>
<th>1</th>
<th>Reliance Industries</th>
<th>104.6 billion USD</th>
</tr>
<tr>
<th>2</th>
<th>Indian Oil Corporation</th>
<th>86 billion USD</th>
</tr>
<tr>
<th>3</th>
<th>Oil and Natural Gas Corporation (ONGC)</th>
<th>61 billion USD</th>
</tr>
<tr>
<th>4</th>
<th>State Bank of India (SBI)</th>
<th>52 billion USD</th>
</tr>
<tr>
<th>5</th>
<th>Tata Motors</th>
<th>44 billion USD</th>
</tr>
</table>
</body>
</html>

"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:

![alt text](<Screenshot 2025-03-22 223246.png>)

![alt text](<Screenshot 2025-03-22 223434.png>)

## Name:D.Nitish Adavan

## Reg no:212224240107

## RESULT:
The program for implementing simple webserver is executed successfully.
