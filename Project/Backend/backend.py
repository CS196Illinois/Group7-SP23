import chess
import chess.engine
board = chess.Board()
print (board)
print(board.legal_moves)

d4 = chess.Move.from_uci("d2d4")
board.push(d4)

print(board)
engine = chess.engine.SimpleEngine.popen_uci(r"C:\Users\anton\Documents\GitHub\Group7-SP23\Project\Backend\stockfish_15.1_win_x64_popcnt\stockfish-windows-2022-x86-64-modern.exe")
#while not board.is_game_over():
result = engine.play(board, chess.engine.Limit(time=0.1))
board.push(result.move)
engine.quit()
print(board)
