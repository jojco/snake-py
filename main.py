# pylint: disable=no-member
import random
import pyxel


class SnakeGame:
    def __init__(self):
        pyxel.init(40, 40, fps=8)
        self.snake_x = [20, 20, 20]
        self.snake_y = [20, 20, 20]
        self.snake_dir = "right"
        self.food_x = 20
        self.food_y = 20
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_UP):
            self.snake_dir = "up"
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.snake_dir = "down"
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.snake_dir = "left"
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.snake_dir = "right"

        # Move the snake
        for i in range(len(self.snake_x)-1, 0, -1):
            self.snake_x[i] = self.snake_x[i-1]
            self.snake_y[i] = self.snake_y[i-1]

        if self.snake_dir == "up":
            self.snake_y[0] -= 2
        elif self.snake_dir == "down":
            self.snake_y[0] += 2
        elif self.snake_dir == "left":
            self.snake_x[0] -= 2
        elif self.snake_dir == "right":
            self.snake_x[0] += 2

        # Check if snake hit the food
        if self.snake_x[0] == self.food_x and self.snake_y[0] == self.food_y:
            self.snake_x.append(self.snake_x[-1])
            self.snake_y.append(self.snake_y[-1])
            self.food_x = random.randint(0, 40)
            self.food_y = random.randint(0, 40)

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.food_x, self.food_y, 1, 1, 1)
        for i in range(len(self.snake_x)):
            pyxel.rect(self.snake_x[i], self.snake_y[i], 4, 4, 8)


if __name__ == "__main__":
    SnakeGame()
