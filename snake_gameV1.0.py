import random

class Snake(object):
    def __init__(self, body, direction):
        self.body = body
        self.direction = direction
    def take_step(self, position):
        self.body = self.body[1:] + [position]
    def set_direction(self,direction):
        self.direction = direction
    def head(self):
        return self.body[-1]
class Apple(object):
    def __init__(self, location):
        self.location = location
class Game(object):
    EMPTY = 0
    BODY = 1
    HEAD = 2
    APPLE = 3

    DISPLAY_CHARS = {
        EMPTY: " ",
        BODY: 'O',
        HEAD: 'X',
        APPLE: '*'
    }

    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    UP_CHAR = 'W'
    DOWN_CHAR = 'S'
    LEFT_CHAR = 'A'
    RIGHT_CHAR = 'D'
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(0, 0), (1, 0), (2, 0), (3, 0)], self.UP)

    def snake_extend_body(self, position):
        self.snake.body = [position] + self.snake.body
    def random_apple_location(self):

        while True:
            apple = (
                random.randint(0, (self.width - 1)),
                random.randint(0, (self.height - 1))
            )

            if apple not in self.snake.body:
                break

        self.current_apple = Apple(apple)



    def next_position(self, position, step):
        return (
            (position[0] + step[0]) % self.width,
            (position[1] + step[1]) % self.height
        )

    def GameBoard(self):

        board = [[self.EMPTY for i in range(self.width)]
                 for j in range(self.height)]

        apple = self.current_apple.location
        board[apple[0]][apple[1]] = self.APPLE

        for body in self.snake.body:
            board[body[0]][body[1]] = self.BODY

        head = self.snake.head()
        board[head[0]][head[1]] = self.HEAD

        return board
    def Play(self):

        self.random_apple_location()

        while True:

            self.render()

            new_direction = input("Enter the your new direction (W,A,S,D): ")
            if new_direction == 'W' and self.snake.direction != self.DOWN:
                self.snake.set_direction(self.UP)
            elif new_direction == 'S' and self.snake.direction != self.UP:
                self.snake.set_direction(self.DOWN)
            elif new_direction == 'A' and self.snake.direction != self.RIGHT:
                self.snake.set_direction(self.LEFT)
            elif new_direction == 'D' and self.snake.direction != self.LEFT:
                self.snake.set_direction(self.RIGHT)

            new_position = self.next_position(self.snake.head(),self.snake.direction)
            if new_position in self.snake.body:
                print("GAME OVER!")
                break

            else:
                self.snake.take_step(new_position)

            if self.current_apple.location == self.snake.head():
                self.random_apple_location()
                self.snake_extend_body(new_position)

    def render(self):
        board = self.GameBoard()

        print("+" + ("-" * self.width) + "+")
        for y in range(self.height):
            line = "|"
            for x in range(self.width):
                cell_val = board[x][self.height-y-1]
                line += self.DISPLAY_CHARS[cell_val]
            line += "|"
            print(line)

        print("+" + ("-" * self.width) + "+")

mygame = Game(15,15)
mygame.Play()

