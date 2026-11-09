"""Simple HTTP server using Python standard library."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

from app.missions import (
    create_mission,
    delete_mission,
    get_active_missions,
    get_mission,
    get_missions,
)


class MissionHandler(BaseHTTPRequestHandler):

    def send_json(self, status_code, payload):
        body = json.dumps(payload).encode("utf-8")

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/missions":
            self.send_json(200, get_missions())
            return

        if path == "/missions/active":
            self.send_json(200, get_active_missions())
            return

        if path.startswith("/missions/"):
            try:
                mission_id = int(path.split("/")[-1])
            except ValueError:
                self.send_json(400, {"error": "Invalid mission ID"})
                return

            mission = get_mission(mission_id)

            if mission is None:
                self.send_json(404, {"error": "Mission not found"})
                return

            self.send_json(200, mission)
            return

        self.send_json(404, {"error": "Route not found"})

    def do_POST(self):
        if urlparse(self.path).path != "/missions":
            self.send_json(404, {"error": "Route not found"})
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length))

            mission = create_mission(
                payload.get("name"),
                payload.get("priority", "medium"),
            )

            self.send_json(201, mission)

        except (ValueError, json.JSONDecodeError) as error:
            self.send_json(400, {"error": str(error)})

    def do_DELETE(self):
        path = urlparse(self.path).path

        try:
            mission_id = int(path.split("/")[-1])
        except ValueError:
            self.send_json(400, {"error": "Invalid mission ID"})
            return

        mission = delete_mission(mission_id)

        if mission is None:
            self.send_json(404, {"error": "Mission not found"})
            return

        self.send_json(200, {"deleted": mission})


def main():
    server = HTTPServer(("127.0.0.1", 8000), MissionHandler)

    print("SpaceRescue API running at http://127.0.0.1:8000")
    print("Press Ctrl+C to stop.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()