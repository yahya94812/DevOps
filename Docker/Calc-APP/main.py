from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

class CalculatorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path != "/calc":
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")
            return

        params = parse_qs(parsed.query)

        try:
            a = float(params.get("a", [None])[0])
            b = float(params.get("b", [None])[0])
            op = params.get("op", [None])[0]

            if a is None or b is None or op is None:
                raise ValueError("Missing parameters")

            if op == "add":
                result = a + b
            elif op == "sub":
                result = a - b
            elif op == "mul":
                result = a * b
            elif op == "div":
                if b == 0:
                    raise ValueError("Division by zero")
                result = a / b
            else:
                raise ValueError("Invalid operation. Use add, sub, mul, or div.")

            response = {"result": result}
            data = json.dumps(response).encode()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(data)

        except Exception as e:
            error = json.dumps({"error": str(e)}).encode()
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(error)


def run():
    server = HTTPServer(("0.0.0.0", 8080), CalculatorHandler)
    print("Server running http://0.0.0.0:8080")
    server.serve_forever()


if __name__ == "__main__":
    run()
