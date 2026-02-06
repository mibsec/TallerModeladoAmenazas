from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "PayFast Core API v1"


if __name__ == '__main__':
    # CORREGIDO: debug=False para produccion (previene exposicion del debugger interactivo)
    app.run(host='0.0.0.0', port=5000, debug=False)
