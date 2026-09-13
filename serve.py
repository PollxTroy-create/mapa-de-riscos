"""Servidor de pré-visualização local do jogo.
Serve HTML como UTF-8 — o host do Artifact injeta o charset por conta
própria, o http.server padrão não, e sem ele os acentos quebram."""
import functools, http.server, os, socketserver

ROOT = os.path.dirname(os.path.abspath(__file__))

class H(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        t = super().guess_type(path)
        return t + "; charset=utf-8" if t in ("text/html", "text/plain") else t

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    handler = functools.partial(H, directory=ROOT)
    with socketserver.TCPServer(("127.0.0.1", 8731), handler) as s:
        print("servindo", ROOT, "em http://localhost:8731")
        s.serve_forever()
