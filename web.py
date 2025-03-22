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