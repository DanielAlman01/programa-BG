import sqlite3
import json
import socketserver
import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer

puerto = 8007

class MiHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/usuarios':
            
            self.send_response(200)
            self.send_header('Content-type', 'application/xml')
            self.end_headers()
            usuarios = obtener_usuarios()
            xml = convertir_a_xml(usuarios)
            self.wfile.write(xml)
        else:
            self.send_response(404)
            self.end_headers()

with socketserver.TCPServer(('', puerto), MiHandler) as servidor:
    print(f'Servidor web iniciado en el puerto {puerto}')

    servidor.serve_forever()