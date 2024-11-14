### Snake Game in Python

A classic Snake game where the player controls a snake to collect apples, grow in length, and avoid colliding with its own body.

---

### 1. `Snake` Class: 🐍

Manages the snake's body, movement, and direction.

- **Attributes**:
  - `body`: List of `(x, y)` tuples representing the snake’s body.
  - `direction`: Current movement direction (e.g., `(0, 1)` for right).

- **Methods**:
  - `take_step()`: Moves the snake one step forward.
  - `set_direction(direction)`: Changes the snake’s movement direction.
  - `head()`: Returns the position of the snake's head.

---

### 2. `Apple` Class: 🍏

Represents the apple that the snake needs to eat to grow.

- **Attributes**:
  - `location`: A tuple `(x, y)` for the apple's position.

---

### 3. `Game` Class: 🎮

Controls the game’s flow, grid rendering, and interaction.

- **Attributes**:
  - `EMPTY`: `" "` (empty space).
  - `BODY`: `"O"` (snake’s body).
  - `HEAD`: `"X"` (snake’s head).
  - `APPLE`: `"*"` (apple).
  - `UP`, `DOWN`, `LEFT`, `RIGHT`: Directional movement tuples.
  - `width`, `height`: Grid dimensions.
  - `snake`: An instance of the `Snake` class.
  - `apple`: An instance of the `Apple` class.

- **Methods**:
  - `random_apple_location()`: Generates a random location for the apple.
  - `render()`: Displays the grid with the snake and apple.
  - `play()`: Main game loop for controlling and updating the game.

---

### 4. Game Flow: 🏁

1. **Initialization**: Set up the snake and apple.
2. **Player Input**: Control snake with `W`, `A`, `S`, `D` keys.
3. **Movement**: Snake moves in the current direction.
4. **Apple Collision**: If the snake eats an apple, it grows.
5. **Game Over**: If the snake collides with itself, the game ends.

---

### Controls: 🕹️

- **W**: Move up
- **A**: Move left
- **S**: Move down
- **D**: Move right

### End Condition: ⚰️

- If the snake collides with itself, the game ends.
--- 

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
