import { Chessboard } from "react-chessboard";
import { useState } from "react";

export default function App() {
  const [position, setPosition] = useState('start');
  function clearBoard() {
    setPosition({});
  }
  function startPosition() {
    setPosition('start');
  }
  function updatePosition(updatedposition) {
    setPosition(updatedposition);
    console.log(updatedposition);
  }
  
  return (
    <><div>
      <Chessboard id="BasicBoard" boardWidth={500} position={position} getPositionObject={updatePosition}/>
      
      <button onClick={clearBoard}>Clear Board</button>
      <button onClick={startPosition}>Start Position</button>
      {/* <button onClick={getPosition}>Get Position</button> */}

    </div><script>
        {/* var board = Chessboard('myBoard', 'start') */}

        {/* $('#clearBoardBtn').on('click', board.clear) */}

        {/* $('#startPositionBtn').on('click', board.start) */}

      </script></>
    
  );
}