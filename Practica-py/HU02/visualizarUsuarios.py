from flask import Flask, Response
import database
import dicttoxml

app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = database.obtener_usuarios()
    usuarios_dict = [{"nombre": u[0], "edad": u[1], "extranjero": u[2]} for u in usuarios]
    xml = dicttoxml.dicttoxml(usuarios_dict, custom_root='usuarios', attr_type=False)
    return Response(xml, mimetype='application/xml')

def iniciar_servidor():
    app.run(debug=True)
