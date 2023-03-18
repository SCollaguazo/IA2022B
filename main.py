from flask import Flask

app = Flask(__name__)
PORT = 5000
DEBUG = False

@app.errorhandler(404)
def not_found(error):
    return "Hubo algun error"

@app.route('/', methods=['GET'])
def index():
    return "HOLA PRUEBA DE MICROSERVICIOS"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
