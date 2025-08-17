from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def show():
    return jsonify({
        "nombre": "Diego Rene Chen Teyul", 
        "album_favorito": "Paraiso"
    })

if __name__ == "__main__":
    print("Servidor corriendo en http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True) # queria actualizarlo en tiempo real