# pylint: disable=no-member
import random
import pyxel


class SnakeGame:
    def __init__(self):
        pyxel.init(160, 120)
        self.snake_x = [40, 30, 20]
        self.snake_y = [60, 60, 60]
        self.snake_dir = "right"
        self.food_x = 80
        self.food_y = 60
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
            self.snake_y[0] -= 1
        elif self.snake_dir == "down":
            self.snake_y[0] += 1
        elif self.snake_dir == "left":
            self.snake_x[0] -= 1
        elif self.snake_dir == "right":
            self.snake_x[0] += 1

        # Check if snake hit the food
        if self.snake_x[0] == self.food_x and self.snake_y[0] == self.food_y:
            self.snake_x.append(self.snake_x[-1])
            self.snake_y.append(self.snake_y[-1])
            self.food_x = random.randint(0, 160)
            self.food_y = random.randint(0, 120)

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.food_x, self.food_y, 3, 3, 9)
        for i in range(len(self.snake_x)):
            pyxel.rect(self.snake_x[i], self.snake_y[i], 3, 3, 7)


if __name__ == "__main__":
    SnakeGame()
