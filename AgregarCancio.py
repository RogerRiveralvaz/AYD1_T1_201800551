from flask import Flask, request, jsonify

app = Flask(__name__)

canciones = []

@app.route('/cancion', methods=['POST'])
def agregar_cancion():
    data = request.get_json()
    nombre = data.get('nombre')
    artista = data.get('artista')
    album = data.get('album')
    
    if not nombre or not artista or not album:
        return jsonify({"error": "Faltan datos"}), 400
    
    cancion = {"nombre": nombre, "artista": artista, "album": album}
    canciones.append(cancion)
    
    return jsonify(cancion), 201
@app.route('/informacion', methods=['GET'])
def obtener_informacion():
    return jsonify({"nombre": "Roger Alberto Rivera Alvarez", "carnet": "201800551"}), 200

if __name__ == '__main__':
    app.run(debug=True)