import pygame
from random import choice
import sys
def maze(WIDTH,HEIGHT,tile=50):
    res = (800, 800)
    cols, rows = WIDTH // tile, HEIGHT // tile
    # colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    orange = (255, 165, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    red=(255,0,0)
    pygame.init()
    screen = pygame.display.set_mode(res, pygame.RESIZABLE)
    clock = pygame.time.Clock()

    class Cell:
        def __init__(self, x, y):
            self.x, self.y = x, y
            self.visited = False
            self.walls = {'Top': True, 'Right': True, 'Left': True, 'Bottom': True}

        def draw_current_cell(self):
            x, y = self.x * tile, self.y * tile
            pygame.draw.rect(screen, orange, (x + 2, y + 2, tile - 2, tile - 2))

        def draw(self):
            x, y = self.x * tile, self.y * tile
            if self.visited:
                pygame.draw.rect(screen, white, (x, y, tile, tile))
            if self.walls['Top']:
                pygame.draw.line(screen, green, (x, y), (x + tile, y), 2)
            if self.walls['Right']:
                pygame.draw.line(screen, green, (x + tile, y), (x + tile, y + tile), 2)
            if self.walls['Left']:
                pygame.draw.line(screen, green, (x, y), (x, y + tile), 2)
            if self.walls['Bottom']:
                pygame.draw.line(screen, green, (x, y + tile), (x + tile, y + tile), 2)

        def check_cells(self, x, y):
            find_index = lambda x, y: x + y * cols
            if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
                return False
            return grid_cells[find_index(x, y)]

        def check_neighbours(self):
            neighbours = []
            top = self.check_cells(self.x, self.y - 1)
            right = self.check_cells(self.x + 1, self.y)
            left = self.check_cells(self.x - 1, self.y)
            bottom = self.check_cells(self.x, self.y + 1)
            if top and not top.visited:
                neighbours.append(top)
            if right and not right.visited:
                neighbours.append(right)
            if left and not left.visited:
                neighbours.append(left)
            if bottom and not bottom.visited:
                neighbours.append(bottom)
            return choice(neighbours) if neighbours else False
        
        def draw_start(self):
            x, y = self.x * tile, self.y * tile
            pygame.draw.rect(screen, red, (x + 2, y + 2, tile - 2, tile - 2))

        def draw_end(self):
            x, y = self.x * tile, self.y * tile
            pygame.draw.rect(screen, green, (x + 2, y + 2, tile - 2, tile - 2))

    def remove_walls(current, next):
        dx = current.x - next.x
        dy = current.y - next.y
        if dx == 1:
            current.walls['Left'] = False
            next.walls['Right'] = False
        elif dx == -1:
            current.walls['Right'] = False
            next.walls['Left'] = False
        if dy == -1:
            current.walls['Bottom'] = False
            next.walls['Top'] = False
        elif dy == 1:
            current.walls['Top'] = False
            next.walls['Bottom'] = False

    def draw_path(path):
        for i in range(len(path) - 1):
            x1, y1 = path[i].x * tile + tile // 2, path[i].y * tile + tile // 2
            x2, y2 = path[i + 1].x * tile + tile // 2, path[i + 1].y * tile + tile // 2
            pygame.draw.line(screen, blue, (x1, y1), (x2, y2), 4)

    grid_cells = [Cell(i, j) for j in range(rows) for i in range(cols)]
    current_cell = grid_cells[0]
    stack = []
    maze_generated = False

    # Function to solve the maze using DFS
    def solve_maze_dfs(start, end):
        stack = [start]
        path = [start]
        visited = set()
        
        while stack:
            current = stack.pop()
            
            if current == end:
                return path
            
            visited.add(current)
            
            # Get neighbors based on the walls
            neighbors = []
            if not current.walls['Top']:
                top = current.check_cells(current.x, current.y - 1)
                if top and top not in visited:
                    neighbors.append(top)
            if not current.walls['Right']:
                right = current.check_cells(current.x + 1, current.y)
                if right and right not in visited:
                    neighbors.append(right)
            if not current.walls['Left']:
                left = current.check_cells(current.x - 1, current.y)
                if left and left not in visited:
                    neighbors.append(left)
            if not current.walls['Bottom']:
                bottom = current.check_cells(current.x, current.y + 1)
                if bottom and bottom not in visited:
                    neighbors.append(bottom)
            
            if neighbors:
                stack.append(current)  
                next_cell = neighbors[0]
                stack.append(next_cell)
                path.append(next_cell)
            else:
                path.pop()  # Remove dead-end from path
        
        return path  # Return the path

    path = None
    while True:
        screen.fill(black)

        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        [cell.draw() for cell in grid_cells]
        
        if not maze_generated:
            current_cell.visited = True
            current_cell.draw_current_cell()

            next_cell = current_cell.check_neighbours()
            if next_cell:
                next_cell.visited = True
                stack.append(current_cell)
                remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif stack:
                current_cell = stack.pop()
            else:
                maze_generated = True
                start_cell = grid_cells[0]
                end_cell = grid_cells[-1]
                path = solve_maze_dfs(start_cell, end_cell)
        else:
            if path:
                grid_cells[0].draw_start()
                grid_cells[-1].draw_end()
                draw_path(path)

        pygame.display.flip()
        clock.tick(30)
