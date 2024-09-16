import http.server
import json
import socketserver

#DEFINIR EL PUERTO EN EL QUE SE EJECUTARA EL SERVIDOR
puerto = 8000

class MiHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header("content-type", "application/json")
        self.end_headers()

        respuesta_json =  {'mensaje':'Hola que hace'}
        
        respuesta_json_srt = json.dumps(respuesta_json)
        self.wfile.write(respuesta_json_srt.encode('utf-8'))

with socketserver.TCPServer(('', puerto), MiHandler) as servidor:
    print(f'Servidor web iniciado en el puerto {puerto}')

    servidor.serve_forever()