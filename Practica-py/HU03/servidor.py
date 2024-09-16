# http_handler.py
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
from database import insert_user, get_users
import json

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        if self.path == '/colaboradores':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode('utf-8')
            params = json.loads(body)

            correo = params.get('correo', '')
            contraseña = params.get('contraseña', '')

            insert_user(correo, contraseña)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Usuario agregado exitosamente'}).encode('utf-8'))

    def do_GET(self):
        if self.path == '/colaboradores':
            users = get_users()
            print(json.dumps(users).encode('utf-8'))

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(users).encode('utf-8'))
