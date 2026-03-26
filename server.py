from http.server import HTTPServer
from app import SimpleAppHandler

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAppHandler)

    print(f"✅ Server successfully started on http://localhost:{port}")
    print("Press Ctrl+C to shut down.")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down the server gracefully...")
        httpd.server_close()
        print("Server stopped.")

if __name__ == "__main__":
    run_server(port=8000)