import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/admin/system_check', methods=['POST'])
def system_check():
    ip = request.json.get('ip')
    return os.popen(f"ping -c 1 {ip}").read()


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return "Query ejecutado: " + query


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
