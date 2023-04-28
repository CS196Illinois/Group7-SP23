from flask import Flask, redirect, url_for, request, jsonify
import chess
import itertools
import os
import chess.engine
import json 
from flask_cors import CORS

stockfishPath =  os.path.dirname(__file__) + "\stockfish\Stockfish.exe"
app = Flask(__name__)
CORS(app)
@app.route("/", methods=["POST"])
# def convert():
    

def hello():
    requestBody = (request.get_json())
    # with open(requestPosition) as json_file:
    #     data = json.load(json_file)
    print("\nTurn:", requestBody['turn'])
    turn = requestBody['turn']
    convertedTurn = ""
    if (turn == "white"):
        convertedTurn = "w"
    elif(turn == "black"):
        convertedTurn = "b"
    arrayAtoH = ["a","b","c","d","e","f","g","h"]
    convertedPossition = ""
    move = requestBody['position']["a8"]
    print(type(move))
    x = 8
    for i in range(8):
        j = 0
        while (j < 8):
            templetter = arrayAtoH[j] + str(x)
            if (templetter not in requestBody['position']):
                y = 0
                while (templetter not in requestBody['position']):
                    y += 1
                    if (j + y >= 8):
                        break
                    templetter = arrayAtoH[j+y] + str(x)
                    
                j += y
                y = str(y)
                convertedPossition += y
                y = int(y)
                
                y = 0
            elif(templetter in requestBody['position']):
                addedPice = requestBody['position'][templetter]
                if(addedPice[0] == "b"):
                    addedPiceConvcerted = addedPice[1].lower()
                elif(addedPice[0] == "w"):
                    addedPiceConvcerted = addedPice[1].upper()
                convertedPossition += addedPiceConvcerted
                j += 1
        convertedPossition += "/"
        x -= 1
    convertedPossition = convertedPossition[0:len(convertedPossition)-1]
    convertedPossition += " " + convertedTurn + " KQkq - 2 4"
    
    print(convertedPossition)
    board = chess.Board(convertedPossition)
    engine = chess.engine.SimpleEngine.popen_uci(stockfishPath)
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
    engine.quit()
    # Replace with chess move-making logic
    print(board.fen()) 
    converted = str(board.fen())
    data = {
        "updatedposition" : converted
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="localhost", port=5002, debug=True)
