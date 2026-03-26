import json
from http.server import BaseHTTPRequestHandler

class SimpleAppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            html_content = """
            <html>
                <head><title>Python Mini Server</title></head>
                <body>
                    <h1>Welcome to the Mini Server!</h1>
                    <p>This server is running on Python 3.13 without external dependencies.</p>
                    <a href="/api/status">Check API Status</a>
                </body>
            </html>
            """
            self.wfile.write(html_content.encode("utf-8"))

        elif self.path == "/api/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            json_data = json.dumps({"status": "success", "message": "Server is running perfectly."})
            self.wfile.write(json_data.encode("utf-8"))

        # Route: 404 Not Found
        else:
            self.send_error(404, f"Page {self.path} not found.")

    def do_POST(self):
        
        if self.path == "/submit":
            # 1. Figure out how much data was sent
            content_length = int(self.headers.get('Content-Length', 0))
            
            # 2. Read the data
            post_data = self.rfile.read(content_length).decode("utf-8")
            
            # 3. Send a response acknowledging receipt
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            response = json.dumps({
                "message": "Data received successfully!",
                "data_received": post_data
            })
            self.wfile.write(response.encode("utf-8"))
        else:
            self.send_error(404, "Endpoint not found.")