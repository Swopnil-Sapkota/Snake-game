import pygame
from food import Food
from snake import Snake
from utils import food_positions, Score, display_game_over

# Initialize pygame and set up the game window, colors, etc.
pygame.init()
window_x = 720
window_y = 480

# Defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialise game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# Create a Food object
food = Food(window_x, window_y)

# Create a Snake object
snake = Snake(window_x, window_y)

# Create a Score object
score = 0

# Game loop
running = True
clock = pygame.time.Clock()
game_over = False

#Add a running variable to control the game loop
while running:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  #Set running to False to exit the game loop
            
    if not game_over:
        snake.move(food.position)

        # Check for key presses to change the snake's direction
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_RIGHT]:
                snake.change_direction('RIGHT')
            if keys[pygame.K_LEFT]:
                snake.change_direction('LEFT')
            if keys[pygame.K_UP]:
                snake.change_direction('UP')
            if keys[pygame.K_DOWN]:
                snake.change_direction('DOWN')

        # Check for collision with food
        if snake.get_head_position() == food.position:
            score += 1
            food.position = food_positions(window_x, window_y, snake.get_body())

        # Check for collision with boarders
        if snake.check_collision():
            game_over = True

        # Fill with a background color
        game_window.fill(black)

        # Display the snake and food objects on the screen
        for position in snake.get_body():
            pygame.draw.rect(game_window, green, pygame.Rect(position[0], position[1], 10, 10))

        food.draw(white)

        # Update and display the score
        score_text, _ = Score(score)
        game_window.blit(score_text, (10, 10))

    else:
        display_game_over(game_window, score)

    pygame.display.update()

# Keep the game window open for a few seconds before quitting
pygame.time.delay()

pygame.quit()