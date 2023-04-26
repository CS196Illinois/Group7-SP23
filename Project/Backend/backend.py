import chess
import chess.engine
from pathlib import Path
board = chess.Board()
print (board)
print(board.legal_moves)



d4 = chess.Move.from_uci("d2d4")
board.push(d4)

print(board)
engine = chess.engine.SimpleEngine.popen_uci("Project\Backend\stockfish\Stockfish.exe")

#while not board.is_game_over():
result = engine.play(board, chess.engine.Limit(time=0.1))
board.push(result.move)
engine.quit()
print(board)
