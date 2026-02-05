import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def process_webhook():
    data = request.json
    callback_url = data.get('url')

    try:
        r = requests.get(callback_url, timeout=2)
        return {"status": "sent", "code": r.status_code}
    except Exception as e:
        return {"error": str(e)}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
