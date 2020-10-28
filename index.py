from flask import Flask, jsonify, request
from diccionario import diccionario

app = Flask(__name__)

#ruta que muestra todas las palabras del diccionario
@app.route('/diccionario')
def getDiccionario():
    return jsonify(diccionario)

#ruta que busca una palabra en especifico del diccionario
@app.route('/diccionario/<string:word>')
def getDic_word(word):
    #w es la palabra que buscas
    word_Found = [w for w in diccionario if w['palabra'] == word]
    if (len(word_Found) > 0):
        return jsonify({"word": word_Found[0]})
    return jsonify({"message": "Word Not Found."})

#esta ruta añade una nueva palabra al diccionario
@app.route('/diccionario', methods=['POST'])
def addDic_word():
    new_word = {
        "id": request.json["id"],
        "palabra": request.json["palabra"],
        "significado": request.json["significado"]
    }
    diccionario.append(new_word)

    return jsonify({"message": "Word Added Succesfully", "diccionario": diccionario})

#ruta para cambiar o editar una palabra
@app.route('/diccionario/<string:word>', methods=["PUT"])
def editDic_word(word):
    word_Found = [w for w in diccionario if w["palabra"] ==  word]
    if (len(word_Found) > 0):
        word_Found[0]["id"] = request.json["id"]
        word_Found[0]["palabra"] = request.json["palabra"]
        word_Found[0]["significado"] = request.json["significado"]
        return jsonify({
            "message": "Word Updated",
            "Word": word_Found[0]
        })
    return jsonify({"message": "Word Not Found"})

@app.route('/diccionario/<string:word>', methods=["DELETE"])
def deleteDic_word(word):
    word_Found = [w for w in diccionario if w["palabra"] == word]
    if len(word_Found) > 0:
        diccionario.remove(word_Found[0])
        return jsonify({
            "message": "Word Deleted",
            "Word": diccionario
        })
    return jsonify({"message": "Word Not Found"})

    
if __name__ == '__main__':
    app.run(debug=True)
