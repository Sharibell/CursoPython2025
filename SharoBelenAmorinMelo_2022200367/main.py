from flask import Flask, request, jsonify
from cliente import cliente

app = Flask(__name__)

@app.route('/cliente', methods=['POST'])
def consultar_cliente():
    data = request.get_json()
    if not data or 'ci' not in data:
        return jsonify({
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": "No proporcionado"
        }), 400

    ci_cliente = data['ci']
    
    if ci_cliente in cliente:
        info_cliente = cliente[ci_cliente]
        respuesta_exitosa = {
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": ci_cliente,
            "nombre": info_cliente["nombre"],
            "apellidos": info_cliente["apellidos"],
            "cel": info_cliente["cel"],
            "dir": info_cliente["dir"]
        }
        return jsonify(respuesta_exitosa), 200
    else:
        respuesta_no_existe = {
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": ci_cliente
        }
        return jsonify(respuesta_no_existe), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003, debug=True)