from flask import Flask

app = Flask(__name__)
PORT = 5000
DEBUG = True

@app.route('/', methods=['GET'])
def index():
    return "HOLA PRUEBA DE MICROSERVICIOS"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
