---

# Snake Game in Python

This is a simple Snake game implemented in Python. The goal of the game is to control the snake, collect apples, and grow the snake's length without hitting the snake's body. The snake moves in a grid, and each step extends its body by one unit. If the snake eats an apple, it grows, and the game continues until the snake crashes into itself.

### Code Explanation:

#### 1. `Snake` Class:
The `Snake` class handles the state and behavior of the snake itself.
- **Attributes**:
  - `body`: A list of tuples representing the coordinates of each part of the snake's body.
  - `direction`: The current movement direction of the snake.
- **Methods**:
  - `take_step(position)`: Moves the snake forward by one position.
  - `set_direction(direction)`: Changes the snake's direction.
  - `head()`: Returns the current position of the snake's head.

#### 2. `Apple` Class:
The `Apple` class represents the apple that the snake needs to eat.
- **Attributes**:
  - `location`: The current coordinates of the apple.

#### 3. `Game` Class:
This is the main class that controls the game logic and display.
- **Attributes**:
  - `EMPTY`, `BODY`, `HEAD`, `APPLE`: Constants used to represent different objects in the game grid (empty space, snake's body, snake's head, and apple).
  - `DISPLAY_CHARS`: A dictionary to map the game objects to visual representations (`'O'` for body, `'X'` for head, `'*'` for apple, and a space for empty cells).
  - `UP`, `DOWN`, `LEFT`, `RIGHT`: Tuples representing the possible directions in which the snake can move.
  - `UP_CHAR`, `DOWN_CHAR`, `LEFT_CHAR`, `RIGHT_CHAR`: Key bindings for user input.
  - `height` and `width`: The size of the game grid.
  - `snake`: An instance of the `Snake` class.
  - `current_apple`: The current apple object in the game.
  
- **Methods**:
  - `snake_extend_body(position)`: Extends the snake's body when it eats an apple.
  - `random_apple_location()`: Places the apple in a random location on the grid, avoiding the snake's body.
  - `next_position(position, step)`: Calculates the next position of the snake based on its current direction.
  - `GameBoard()`: Builds the game board based on the current state of the snake and the apple.
  - `Play()`: The main loop of the game, where the snake moves, the user inputs the direction, and the game ends if the snake crashes into itself.
  - `render()`: Renders the game board to the console.

#### 4. Game Flow:
- The game starts by initializing the snake and randomly placing an apple.
- The player controls the snake using `W`, `A`, `S`, and `D` keys to move up, left, down, and right, respectively.
- If the snake collides with its own body, the game ends.
- Each time the snake eats an apple, it grows, and a new apple is placed on the grid.

---


## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
