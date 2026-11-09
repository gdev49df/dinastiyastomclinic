#!/usr/bin/env python3
"""Локальный сервер с адресами без .html (как на github pages).

Запуск из любой папки:  python3 tools/serve.py   ->  http://localhost:8000
"""
import http.server
import os
import socketserver

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(os.environ.get("PORT", "8000"))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def translate_path(self, path):
        full = super().translate_path(path)
        if not os.path.exists(full) and os.path.exists(full + ".html"):
            return full + ".html"
        return full

    def send_error(self, code, message=None, explain=None):
        """Для несуществующих адресов отдаём 404.html, как github pages."""
        page = os.path.join(ROOT, "404.html")
        if code == 404 and os.path.exists(page):
            with open(page, "rb") as f:
                body = f.read()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)
            return
        super().send_error(code, message, explain)


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as srv:
        print(f"http://localhost:{PORT}")
        srv.serve_forever()
