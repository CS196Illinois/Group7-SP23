import { Chessboard } from "react-chessboard";

export default function App() {
  return (
    <><div>
      <Chessboard id="BasicBoard" boardWidth={500} />

      <button id="clearBoardBtn">Clear Board</button>
      <button id="startPositionBtn">Start Position</button>
      <button id="clearBoardInstantBtn">Clear Board Instant</button>

    </div><script>
        var board = Chessboard('myBoard', 'start')

        $('#clearBoardBtn').on('click', board.clear)

        $('#startPositionBtn').on('click', board.start)

      </script></>
    
  );
}