from flask import Flask, redirect, url_for
import chess
import itertools

app = Flask(__name__)
board = chess.Board("rnbqkbnr/pppp1Qpp/8/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
@app.route("/")
def hello():
    print(board) 
    converted = str(board)
    return (converted)

if __name__ == "__main__":
    app.run()
