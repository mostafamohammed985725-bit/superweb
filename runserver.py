from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import socket
import security  # 🔒 ملف الحماية

PORT = 47823  # منفذ غير مشهور
WEB_DIR = os.path.dirname(os.path.abspath(__file__))

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]
        path = self.path
        user_agent = self.headers.get("User-Agent", "")

        # 🔒 فحص الحماية
        if not security.is_allowed(client_ip, path, user_agent):
            self.send_error(403, "Access Denied")
            return

        # عرض الصفحة فقط
        with open(os.path.join(WEB_DIR, "index.html"), "rb") as f:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f.read())

# تشغيل السيرفر
server = HTTPServer(("0.0.0.0", PORT), MyHandler)

# طباعة IP (اختياري)
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
print(f"🔐 Secure Server Running: http://{IP}:{PORT}")

server.serve_forever()