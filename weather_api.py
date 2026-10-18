from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time

START_TIME = time.time()

class WeatherAPI(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):
        body = json.dumps(data).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-cache")
        self.send_header("X-IoT-Protocol", "HTTP-REST")
        self.end_headers()

        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/current":
            self.send_json({
                "temperature": 22.8,
                "humidity": 54,
                "pressure": 1012.6
            })

        elif self.path == "/status":
            self.send_json({
                "status": "online",
                "uptime": round(time.time() - START_TIME)
            })

        elif self.path == "/devices":
            self.send_json({
                "lamp": "ON",
                "brightness": 75,
                "fan": "ON"
            })

        else:
            self.send_json({
                "error": "Endpoint not found"
            }, 404)


server = HTTPServer(("localhost", 8090), WeatherAPI)

print("Weather REST API started")
print("http://localhost:8090/current")
print("http://localhost:8090/status")
print("http://localhost:8090/devices")

server.serve_forever()