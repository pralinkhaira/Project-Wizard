const COLS = 10;
const ROWS = 20;
let BLOCK_SIZE = 30;

const COLOR_MAPPING = [
  "#E74C3C", // darker modern red
  "#E67E22", // darker modern orange
  "#16A085", // darker modern teal
  "#8E44AD", // darker modern purple
  "#2980B9", // darker modern blue
  "#138F7A", // darker modern turquoise
  "#F39C12", // darker modern yellow
  "#95A5A6", // darker modern grey for empty cells
];

const drawCell = (xAxis, yAxis, colorId) => {
  ctx.fillStyle = COLOR_MAPPING[colorId] || COLOR_MAPPING[WHITE_COLOR_ID];
  ctx.fillRect(xAxis * BLOCK_SIZE, yAxis * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
};

const BRICK_LAYOUT = [
  [
    [
      [1, 7, 7],
      [1, 1, 1],
      [7, 7, 7],
    ],
    [
      [7, 1, 1],
      [7, 1, 7],
      [7, 1, 7],
    ],
    [
      [7, 7, 7],
      [1, 1, 1],
      [7, 7, 1],
    ],
    [
      [7, 1, 7],
      [7, 1, 7],
      [1, 1, 7],
    ],
  ],
  [
    [
      [7, 1, 7],
      [7, 1, 7],
      [7, 1, 1],
    ],
    [
      [7, 7, 7],
      [1, 1, 1],
      [1, 7, 7],
    ],
    [
      [1, 1, 7],
      [7, 1, 7],
      [7, 1, 7],
    ],
    [
      [7, 7, 1],
      [1, 1, 1],
      [7, 7, 7],
    ],
  ],
  [
    [
      [1, 7, 7],
      [1, 1, 7],
      [7, 1, 7],
    ],
    [
      [7, 1, 1],
      [1, 1, 7],
      [7, 7, 7],
    ],
    [
      [7, 1, 7],
      [7, 1, 1],
      [7, 7, 1],
    ],
    [
      [7, 7, 7],
      [7, 1, 1],
      [1, 1, 7],
    ],
  ],
  [
    [
      [7, 1, 7],
      [1, 1, 7],
      [1, 7, 7],
    ],
    [
      [1, 1, 7],
      [7, 1, 1],
      [7, 7, 7],
    ],
    [
      [7, 7, 1],
      [7, 1, 1],
      [7, 1, 7],
    ],
    [
      [7, 7, 7],
      [1, 1, 7],
      [7, 1, 1],
    ],
  ],
  [
    [
      [7, 7, 7, 7],
      [1, 1, 1, 1],
      [7, 7, 7, 7],
      [7, 7, 7, 7],
    ],
    [
      [7, 7, 1, 7],
      [7, 7, 1, 7],
      [7, 7, 1, 7],
      [7, 7, 1, 7],
    ],
    [
      [7, 7, 7, 7],
      [7, 7, 7, 7],
      [1, 1, 1, 1],
      [7, 7, 7, 7],
    ],
    [
      [7, 1, 7, 7],
      [7, 1, 7, 7],
      [7, 1, 7, 7],
      [7, 1, 7, 7],
    ],
  ],
  [
    [
      [7, 7, 7, 7],
      [7, 1, 1, 7],
      [7, 1, 1, 7],
      [7, 7, 7, 7],
    ],
    [
      [7, 7, 7, 7],
      [7, 1, 1, 7],
      [7, 1, 1, 7],
      [7, 7, 7, 7],
    ],
    [
      [7, 7, 7, 7],
      [7, 1, 1, 7],
      [7, 1, 1, 7],
      [7, 7, 7, 7],
    ],
    [
      [7, 7, 7, 7],
      [7, 1, 1, 7],
      [7, 1, 1, 7],
      [7, 7, 7, 7],
    ],
  ],
  [
    [
      [7, 1, 7],
      [1, 1, 1],
      [7, 7, 7],
    ],
    [
      [7, 1, 7],
      [7, 1, 1],
      [7, 1, 7],
    ],
    [
      [7, 7, 7],
      [1, 1, 1],
      [7, 1, 7],
    ],
    [
      [7, 1, 7],
      [1, 1, 7],
      [7, 1, 7],
    ],
  ],
];

const KEY_CODES = {
  LEFT: "ArrowLeft",
  RIGHT: "ArrowRight",
  UP: "ArrowUp",
  DOWN: "ArrowDown",
};

const WHITE_COLOR_ID = 7;

function resizeCanvas() {

  const canvas = document.getElementById("board");
  const container = document.querySelector('.container');

  // Compute available height inside container (account for small padding/borders)
  const availableHeight = Math.max(0, container.clientHeight - 16);

  // Compute available width more precisely by subtracting the remote panel width
  const remoteEl = document.getElementById('remote');
  const cs = window.getComputedStyle(container);
  let gap = parseFloat(cs.gap || cs.columnGap || 20);
  if (Number.isNaN(gap)) gap = 20;

  let remoteWidth = 0;
  if (remoteEl) {
    // Use layout width of the remote panel (includes padding/border)
    remoteWidth = remoteEl.getBoundingClientRect().width;
  } else {
    // Fallback to roughly 30% of container if remote not present
    remoteWidth = container.clientWidth * 0.3;
  }

  // On narrow screens use full width (stacked layout) — keep a small margin
  let availableWidth = container.clientWidth - remoteWidth - gap - 16;
  if (window.innerWidth <= 600) {
    availableWidth = Math.max(0, container.clientWidth - 24);
  }

  // Determine block size by both axes and take the smaller so cells stay square
  const blockSizeByHeight = Math.floor(availableHeight / ROWS);
  const blockSizeByWidth = Math.floor(availableWidth / COLS);
  BLOCK_SIZE = Math.min(blockSizeByHeight, blockSizeByWidth);
  BLOCK_SIZE = Math.max(BLOCK_SIZE, 20);

  // Apply canvas pixel dimensions (these control the drawing space)
  canvas.width = COLS * BLOCK_SIZE;
  canvas.height = ROWS * BLOCK_SIZE;

  // Set CSS size to match drawing size — this prevents flexbox from stretching it
  canvas.style.width = canvas.width + 'px';
  canvas.style.height = canvas.height + 'px';
  if (canvas.getContext) {
    try { canvas.getContext('2d').imageSmoothingEnabled = false; } catch (e) {}
  }
}

const canvas = document.getElementById("board");
const ctx = canvas.getContext("2d");

// Initial resize
resizeCanvas();

// Resize on window resize
window.addEventListener('resize', resizeCanvas);

class Board {
  constructor(ctx) {
    this.ctx = ctx;
    this.grid = this.generateWhiteBoard();
    this.score = 0;
    this.gameOver = false;
    this.isPlaying = false;

    this.clearAudio = new Audio("../sounds/clear.wav");
    this.clearAudio.preload = 'none'; // Don't preload to avoid 404 errors
  }

  reset() {
    this.score = 0;
    this.grid = this.generateWhiteBoard();
    this.gameOver = false;
    this.drawBoard();
  }

  generateWhiteBoard() {
    return Array.from({ length: ROWS }, () => Array(COLS).fill(WHITE_COLOR_ID));
  }

  drawCell(xAxis, yAxis, colorId) {
    // xAxis => 1 yAxis => 1
    this.ctx.fillStyle =
      COLOR_MAPPING[colorId] || COLOR_MAPPING[WHITE_COLOR_ID];
    this.ctx.fillRect(
      xAxis * BLOCK_SIZE,
      yAxis * BLOCK_SIZE,
      BLOCK_SIZE,
      BLOCK_SIZE
    );
    this.ctx.fillStyle = "black";
    this.ctx.strokeRect(
      xAxis * BLOCK_SIZE,
      yAxis * BLOCK_SIZE,
      BLOCK_SIZE,
      BLOCK_SIZE
    );
  }

  drawBoard() {
    for (let row = 0; row < this.grid.length; row++) {
      for (let col = 0; col < this.grid[0].length; col++) {
        this.drawCell(col, row, this.grid[row][col]);
      }
    }
  }

  handleCompleteRows() {
    const latestGrid = board.grid.filter((row) => {
      // row => []
      return row.some((col) => col === WHITE_COLOR_ID);
    });

    const newScore = ROWS - latestGrid.length; 
    const newRows = Array.from({ length: newScore }, () =>
      Array(COLS).fill(WHITE_COLOR_ID)
    );

    if (newScore) {
      board.grid = [...newRows, ...latestGrid];
      this.handleScore(newScore * 10);

      try {
        this.clearAudio.play();
      } catch (error) {
        // Sound file not available, continue silently
      }
      console.log({ latestGrid });
    }
  }

  handleScore(newScore) {
    this.score += newScore;
    document.getElementById("score").innerHTML = this.score;
  }

  handleGameOver() {
    this.gameOver = true;
    this.isPlaying = false;
    alert("GAME OVER!!!");
  }
}

class Brick {
  constructor(id) {
    this.id = id;
    this.layout = BRICK_LAYOUT[id];
    this.activeIndex = 0;
    this.colPos = 3;
    this.rowPos = -2;
  }

  draw() {
    for (let row = 0; row < this.layout[this.activeIndex].length; row++) {
      for (let col = 0; col < this.layout[this.activeIndex][0].length; col++) {
        if (this.layout[this.activeIndex][row][col] !== WHITE_COLOR_ID) {
          board.drawCell(col + this.colPos, row + this.rowPos, this.id);
        }
      }
    }
  }

  clear() {
    for (let row = 0; row < this.layout[this.activeIndex].length; row++) {
      for (let col = 0; col < this.layout[this.activeIndex][0].length; col++) {
        if (this.layout[this.activeIndex][row][col] !== WHITE_COLOR_ID) {
          board.drawCell(col + this.colPos, row + this.rowPos, WHITE_COLOR_ID);
        }
      }
    }
  }

  moveLeft() {
    if (
      !this.checkCollision(
        this.rowPos,
        this.colPos - 1,
        this.layout[this.activeIndex]
      )
    ) {
      this.clear();
      this.colPos--;
      this.draw();
    }
  }

  moveRight() {
    if (
      !this.checkCollision(
        this.rowPos,
        this.colPos + 1,
        this.layout[this.activeIndex]
      )
    ) {
      this.clear();
      this.colPos++;
      this.draw();
    }
  }

  moveDown() {
    if (
      !this.checkCollision(
        this.rowPos + 1,
        this.colPos,
        this.layout[this.activeIndex]
      )
    ) {
      this.clear();
      this.rowPos++;
      this.draw();

      return;
    }

    this.handleLanded();
    generateNewBrick();
  }

  rotate() {
    if (
      !this.checkCollision(
        this.rowPos,
        this.colPos,
        this.layout[(this.activeIndex + 1) % 4]
      )
    ) {
      this.clear();
      this.activeIndex = (this.activeIndex + 1) % 4;
      /**
       * activeindex = 0
       * 0 + 1 = 1 % 4 ==> 1
       *
       * activeIndex = 3
       * 3 + 1 = 4 % 4 ==> 0
       *
       * **/
      this.draw();
    }
  }

  checkCollision(nextRow, nextCol, nextLayout) {
    // if (nextCol < 0) return true;

    for (let row = 0; row < nextLayout.length; row++) {
      for (let col = 0; col < nextLayout[0].length; col++) {
        if (nextLayout[row][col] !== WHITE_COLOR_ID && nextRow >= 0) {
          if (
            col + nextCol < 0 ||
            col + nextCol >= COLS ||
            row + nextRow >= ROWS ||
            board.grid[row + nextRow][col + nextCol] !== WHITE_COLOR_ID
          )
            return true;
        }
      }
    }

    return false;
  }

  handleLanded() {
    if (this.rowPos <= 0) {
      board.handleGameOver();
      return;
    }

    for (let row = 0; row < this.layout[this.activeIndex].length; row++) {
      for (let col = 0; col < this.layout[this.activeIndex][0].length; col++) {
        if (this.layout[this.activeIndex][row][col] !== WHITE_COLOR_ID) {
          board.grid[row + this.rowPos][col + this.colPos] = this.id;
        }
      }
    }

    board.handleCompleteRows();
    board.drawBoard();
  }
}

function generateNewBrick() {
  brick = new Brick(Math.floor(Math.random() * 10) % BRICK_LAYOUT.length); 
}

board = new Board(ctx);
board.drawBoard();

document.getElementById("play").addEventListener("click", () => {
  board.reset();
  board.isPlaying = true;
  generateNewBrick();
  const refresh = setInterval(() => {
    if (!board.gameOver) {
      brick.moveDown();
    } else {
      clearInterval(refresh);
    }
  }, 1000);
});

// Make control buttons work
document.getElementById("left").addEventListener("click", () => {
  if (!board.gameOver && board.isPlaying) brick.moveLeft();
});
document.getElementById("right").addEventListener("click", () => {
  if (!board.gameOver && board.isPlaying) brick.moveRight();
});
document.getElementById("down").addEventListener("click", () => {
  if (!board.gameOver && board.isPlaying) brick.moveDown();
});
document.getElementById("up").addEventListener("click", () => {
  if (!board.gameOver && board.isPlaying) brick.rotate();
});

document.addEventListener("keydown", (e) => {
  if (!board.gameOver && board.isPlaying) {
    console.log({ e });
    switch (e.code) {
      case KEY_CODES.LEFT:
        brick.moveLeft();
        break;
      case KEY_CODES.RIGHT:
        brick.moveRight();
        break;
      case KEY_CODES.DOWN:
        brick.moveDown();
        break;
      case KEY_CODES.UP:
        brick.rotate();
        break;
      default:
        break;
    }
  }
});


console.table(board.grid);