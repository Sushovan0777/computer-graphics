from maze_generator_solver import maze
import pygame
import sys

pygame.init()

# Screen dimensions
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze simulation using DFS algorithm")

# Colors
BLACK = (0, 0, 0)
NEON_BLUE = (0, 255, 255)
NEON_GREEN = (57, 255, 20)
NEON_PINK = (255, 20, 147)
NEON_ORANGE = (255, 140, 0)
NEON_YELLOW = (255, 255, 0)
START_BUTTON_COLOR = NEON_GREEN

# Fonts
font = pygame.font.Font(None, 36)
label_font = pygame.font.Font(None, 24)

# Initial values
rows, cols, tile_size = 800, 1200, 50

# Input boxes
input_boxes = [
    {"rect": pygame.Rect(150, 100, 140, 40), "text": str(rows), "type": "rows"},
    {"rect": pygame.Rect(150, 150, 140, 40), "text": str(cols), "type": "cols"},
    {"rect": pygame.Rect(150, 200, 140, 40), "text": str(tile_size), "type": "tile_size"}
]

# Buttons
buttons = [
    {"rect": pygame.Rect(300, 100, 40, 40), "text": "+", "action": "increment", "type": "rows"},
    {"rect": pygame.Rect(350, 100, 40, 40), "text": "-", "action": "decrement", "type": "rows"},
    {"rect": pygame.Rect(300, 150, 40, 40), "text": "+", "action": "increment", "type": "cols"},
    {"rect": pygame.Rect(350, 150, 40, 40), "text": "-", "action": "decrement", "type": "cols"},
    {"rect": pygame.Rect(300, 200, 40, 40), "text": "+", "action": "increment", "type": "tile_size"},
    {"rect": pygame.Rect(350, 200, 40, 40), "text": "-", "action": "decrement", "type": "tile_size"}
]

# Labels
labels = [
    {"text": "Height:", "pos": (50, 110)},
    {"text": "Width:", "pos": (50, 160)},
    {"text": "Tile Size:", "pos": (50, 210)}
]

# Title
title = {"text": "Enter the Height,Width and tile size of Maze", "pos": (50, 50)}

# Start button
start_button = {"rect": pygame.Rect(150, 300, 100, 50), "text": "Start"}

# Active input box
active_box = None

# Function to handle input events
def handle_input(event, box):
    if event.key == pygame.K_BACKSPACE:
        box["text"] = box["text"][:-1]
    elif event.unicode.isdigit():
        box["text"] += event.unicode

# Function to update the values based on button clicks
def update_value(action, type_):
    global rows, cols, tile_size
    if type_ == "rows":
        if action == "increment" and rows <= 700:
            rows += 100
        elif action == "decrement" and rows >= 400:
            rows -= 100
    elif type_ == "cols":
        if action == "increment" and cols <= 1400:
            cols += 100
        elif action == "decrement" and cols >= 500:
            cols -= 100
    elif type_ == "tile_size":
        if action == "increment" and tile_size < 50:
            tile_size += 5
        elif action == "decrement" and tile_size > 10:
            tile_size -= 5

# Function to handle the start button click
def start():
    print(f"Starting with rows: {rows}, cols: {cols}, tile size: {tile_size}")
    maze(cols,rows,tile_size)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button["rect"].collidepoint(event.pos):
                start()
                
            for box in input_boxes:
                if box["rect"].collidepoint(event.pos):
                    active_box = box
                    break
            else:
                active_box = None

            for button in buttons:
                if button["rect"].collidepoint(event.pos):
                    update_value(button["action"], button["type"])

        elif event.type == pygame.KEYDOWN and active_box:
            handle_input(event, active_box)

    # Update input box texts
    input_boxes[0]["text"] = str(rows)
    input_boxes[1]["text"] = str(cols)
    input_boxes[2]["text"] = str(tile_size)

    # Clear the screen
    screen.fill(BLACK)

    # Draw title
    title_surface = font.render(title["text"], True, NEON_BLUE)
    screen.blit(title_surface, title["pos"])

    # Draw input box labels
    for label in labels:
        label_surface = label_font.render(label["text"], True, NEON_PINK)
        screen.blit(label_surface, label["pos"])

    # Draw input boxes
    for box in input_boxes:
        pygame.draw.rect(screen, NEON_ORANGE if box == active_box else NEON_YELLOW, box["rect"], 2)
        txt_surface = font.render(box["text"], True, NEON_GREEN)
        screen.blit(txt_surface, (box["rect"].x + 5, box["rect"].y + 5))

    # Draw buttons
    for button in buttons:
        pygame.draw.rect(screen, NEON_BLUE, button["rect"], 2)
        txt_surface = font.render(button["text"], True, NEON_GREEN)
        screen.blit(txt_surface, (button["rect"].x + 5, button["rect"].y + 5))

    # Draw start button
    pygame.draw.rect(screen, START_BUTTON_COLOR, start_button["rect"])
    start_txt_surface = font.render(start_button["text"], True, BLACK)
    screen.blit(start_txt_surface, (start_button["rect"].x + 10, start_button["rect"].y + 10))

    # Update the display
    pygame.display.flip()

