class Snake:
    def __init__(self, window_x, window_y):
        self.window_x = window_x
        self.window_y = window_y
        self.snake_position = [100, 50]  # Initial position of the snake
        self.snake_body = [[100, 50], [90, 50], [80, 50]]  # Snake body (head + segments)
        self.direction = 'RIGHT'  # Initial direction
        self.change_to = self.direction

    def change_direction(self, new_direction):
        if new_direction == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = 'RIGHT'
        if new_direction == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = 'LEFT'
        if new_direction == 'UP' and not self.direction == 'DOWN':
            self.direction = 'UP'
        if new_direction == 'DOWN' and not self.direction == 'UP':
            self.direction = 'DOWN'

    def move(self, food_position):
        if self.direction == 'RIGHT':
            self.snake_position[0] += 10
        if self.direction == 'LEFT':
            self.snake_position[0] -= 10
        if self.direction == 'UP':
            self.snake_position[1] -= 10
        if self.direction == 'DOWN':
            self.snake_position[1] += 10

        self.snake_body.insert(0, list(self.snake_position))

        if self.snake_position == food_position:
            return True
        else:
            self.snake_body.pop()
            return False

    def check_collision(self):
        if (
            self.snake_position[0] >= self.window_x
            or self.snake_position[0] <= 0
            or self.snake_position[1] >= self.window_y
            or self.snake_position[1] <= 0
        ):
            return True
        for segment in self.snake_body[1:]:
            if self.snake_position == segment:
                return True
        return False

    def get_head_position(self):
        return self.snake_position

    def get_body(self):
        return self.snake_body
