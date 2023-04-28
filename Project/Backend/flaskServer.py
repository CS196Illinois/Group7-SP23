from flask import Flask, redirect, url_for, request
import chess
import itertools
import os
import chess.engine
import json 

stockfishPath =  os.path.dirname(__file__) + "\stockfish\Stockfish.exe"
app = Flask(__name__)

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
        for j in range(8):
            templetter = arrayAtoH[j] + str(x)
            if (templetter not in requestBody['position']):
                y = 0
                while (templetter not in requestBody['position']):
                    y += 1
                    if (j + y > 8):
                        break
                    templetter = arrayAtoH[j+y] + str(x)
                    
                j = y
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
        convertedPossition += "/"
        x -= 1
    convertedPossition = convertedPossition[0:len(convertedPossition)-1]
    convertedPossition += " " + convertedTurn + " KQkq - 2 4"
    
    print(convertedPossition)
    board = chess.Board("r1bqkbnr/p1pp1ppp/1pn5/4p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQkq - 2 4")
    engine = chess.engine.SimpleEngine.popen_uci(stockfishPath)
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
    engine.quit()
    # Replace with chess move-making logic
    print(board) 
    converted = str(board)
    return (converted)

if __name__ == "__main__":
    app.run(host="localhost", port=5002, debug=True)
