import { Chessboard } from "react-chessboard";
import { useState } from "react";

export default function App() {
  const [position, setPosition] = useState('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR');
  function clearBoard() {
    setPosition({});
  }
  function startPosition() {
    setPosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR');
  }
  function updatePosition(updatedposition) {
    setPosition(updatedposition);
    console.log(updatedposition);
  }
  
  let bturn = {"turn":"black",position};
  let wturn = {"turn":"white",position};
  function submitPositionB() {
   fetch('http://localhost:3000/', {
     method: 'POST',
     headers: {"Content-Type": "application/json" },
     body: JSON.stringify(bturn)
   }).then(() => {
     console.log(bturn);
   })
  }
  function submitPositionW() {
    fetch('http://localhost:3000/', {
      method: 'POST',
      headers: {"Content-Type": "application/json" },
      body: JSON.stringify(wturn)
    }).then(() => {
      console.log(wturn);
    })
   }
  return (
    <><div>
      <Chessboard id="BasicBoard" boardWidth={500} position={position} getPositionObject={updatePosition}/>
      
      <button onClick={clearBoard}>Clear Board</button>
      <button onClick={startPosition}>Start Position</button>
      <button onClick={submitPositionB}>Submit Position for Black</button>
      <button onClick={submitPositionW}>Submit Position for White</button>
      {/* <button onClick={getPosition}>Get Position</button> */}

    </div><script>
        {/* var board = Chessboard('myBoard', 'start') */}

        {/* $('#clearBoardBtn').on('click', board.clear) */}

        {/* $('#startPositionBtn').on('click', board.start) */}

      </script></>
    
  );
}