import logging
from urllib.parse import urlparse

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
logger = logging.getLogger(__name__)

# Lista de dominios permitidos para callbacks (whitelist)
ALLOWED_CALLBACK_HOSTS = [
    "api.payfast.com",
    "hooks.payfast.com",
]


def is_url_allowed(url):
    """Valida que la URL sea segura y este en la whitelist de dominios."""
    try:
        parsed = urlparse(url)
    except Exception:
        return False

    # Solo permitir HTTPS
    if parsed.scheme != "https":
        return False

    # Bloquear IPs privadas / internas / metadata de cloud
    hostname = parsed.hostname
    if not hostname:
        return False

    # Verificar contra whitelist de dominios permitidos
    if hostname not in ALLOWED_CALLBACK_HOSTS:
        return False

    return True


@app.route('/webhook', methods=['POST'])
def process_webhook():
    data = request.json
    if not data or 'url' not in data:
        return jsonify({"error": "Campo 'url' requerido"}), 400

    callback_url = data.get('url')

    # Validar URL contra whitelist (previene SSRF)
    if not is_url_allowed(callback_url):
        return jsonify({"error": "URL de callback no permitida"}), 403

    try:
        r = requests.get(callback_url, timeout=5, allow_redirects=False)
        return jsonify({"status": "sent", "code": r.status_code})
    except requests.RequestException:
        # CORREGIDO: no exponer detalles internos del error
        logger.exception("Error al procesar webhook callback")
        return jsonify({"error": "No se pudo contactar el servicio de callback"}), 502


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
