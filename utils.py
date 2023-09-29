import pygame
import random

def food_positions(window_x, window_y, snake_body):
    while True:
        food_position = [random.randrange(1, (window_x // 10)) * 10,
                         random.randrange(1, (window_y // 10)) * 10]
        # Check that the generated position is not on the snake's body
        if food_position not in snake_body:
            return food_position

def Score(score):
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    return score_text, score

def display_game_over(game_window, score):
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("GAME OVER!!", True, (255, 0, 0))
    score_text = font.render(f"Final Score: {score}", True, (0, 0, 255))
    game_window.blit(game_over_text, (game_window.get_width() // 2 - 160, game_window.get_height() // 2 - 50))
    game_window.blit(score_text, (game_window.get_width() // 2 - 160, game_window.get_height() // 2 + 50))
    pygame.display.update()
