import ipaddress
import subprocess

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/admin/system_check', methods=['POST'])
def system_check():
    ip = request.json.get('ip', '')

    # Validar que el input sea una direccion IP valida (previene Command Injection)
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return jsonify({"error": "Direccion IP invalida"}), 400

    # Usar subprocess con lista de argumentos (sin shell=True) para evitar inyeccion
    result = subprocess.run(
        ["ping", "-c", "1", ip],
        capture_output=True,
        text=True,
        timeout=10
    )
    return jsonify({"output": result.stdout})


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', '')

    # Validar input basico
    if not username or len(username) > 150:
        return jsonify({"error": "Username invalido"}), 400

    # Usar consultas parametrizadas para prevenir SQL Injection
    # En produccion se usaria un ORM o conexion real con parametros
    query = "SELECT * FROM users WHERE username = %s"
    params = (username,)
    return jsonify({"query": query, "params": params})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
