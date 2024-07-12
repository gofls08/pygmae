import pygame
import sys
import random
from pygame.locals import *

pygame.init()

FPS = 10
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

def draw_snake(snake_coords):
    for coord in snake_coords:
        x, y = coord['x'] * CELL_SIZE, coord['y'] * CELL_SIZE
        pygame.draw.rect(display_surface, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

def draw_apple(coord):
    x, y = coord['x'] * CELL_SIZE, coord['y'] * CELL_SIZE
    pygame.draw.rect(display_surface, RED, (x, y, CELL_SIZE, CELL_SIZE))

def run_game():
    start_x = random.randint(5, WINDOW_WIDTH // CELL_SIZE - 6)
    start_y = random.randint(5, WINDOW_HEIGHT // CELL_SIZE - 6)
    snake_coords = [{'x': start_x, 'y': start_y},
                    {'x': start_x - 1, 'y': start_y},
                    {'x': start_x - 2, 'y': start_y}]
    direction = 'right'

    apple_x = random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1)
    apple_y = random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1)
    apple = {'x': apple_x, 'y': apple_y}

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print("bye")
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP and direction != 'down':
                    direction = 'up'
                elif event.key == K_DOWN and direction != 'up':
                    direction = 'down'
                elif event.key == K_LEFT and direction != 'right':
                    direction = 'left'
                elif event.key == K_RIGHT and direction != 'left':
                    direction = 'right'

        if direction == 'up':
            new_head = {'x': snake_coords[0]['x'], 'y': snake_coords[0]['y'] - 1}
        elif direction == 'down':
            new_head = {'x': snake_coords[0]['x'], 'y': snake_coords[0]['y'] + 1}
        elif direction == 'left':
            new_head = {'x': snake_coords[0]['x'] - 1, 'y': snake_coords[0]['y']}
        elif direction == 'right':
            new_head = {'x': snake_coords[0]['x'] + 1, 'y': snake_coords[0]['y']}

        snake_coords.insert(0, new_head)

        if (new_head['x'] == apple['x'] and new_head['y'] == apple['y']):
            apple_x = random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1)
            apple_y = random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1)
            apple = {'x': apple_x, 'y': apple_y}
        else:
            del snake_coords[-1]

        display_surface.fill(WHITE)
        draw_snake(snake_coords)
        draw_apple(apple)
        pygame.display.update()

        if (new_head['x'] < 0 or new_head['x'] >= WINDOW_WIDTH // CELL_SIZE or
            new_head['y'] < 0 or new_head['y'] >= WINDOW_HEIGHT // CELL_SIZE or
            new_head in snake_coords[1:]):
            print("end")
            return

        fps_clock.tick(FPS)

fps_clock = pygame.time.Clock()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

def main_menu():
    while True:
        display_surface.fill(WHITE)
        
        play_button = pygame.Rect(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2, 100, 40)
        
        pygame.draw.rect(display_surface, GREEN, play_button)
        play_text = pygame.font.Font(None, 30).render("Play", True, BLACK)
        
        display_surface.blit(play_text, play_button.move(20, 10))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                print("hi")
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                
                if play_button.collidepoint(mouse_x, mouse_y):
                    print("i")
                    return
        
        pygame.display.update()
        fps_clock.tick(FPS)


while True:
    main_menu()
    run_game()
