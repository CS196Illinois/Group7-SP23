import chess
import chess.engine
from pathlib import Path
import os
board = chess.Board()
stockfishPath =  os.path.dirname(__file__) + "\stockfish\Stockfish.exe"

print (board)
print(board.legal_moves)


d4 = chess.Move.from_uci("d2d4")
board.push(d4)

print(board)
engine = chess.engine.SimpleEngine.popen_uci(stockfishPath)

#while not board.is_game_over():
result = engine.play(board, chess.engine.Limit(time=0.1))
board.push(result.move)
engine.quit()
print(board)
