import pygame
import sys
#Initialize Pygame
pygame.init()

# Set up the display

WIDTH,HEIGHT = 800,800
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line Drawing Algorithm")

# Colors

GOLD= (255, 215, 0)

BLACK =(0, 0, 0)

#Function to draw a line using DDA algorithm 
def draw_line_dda(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    steps = max(abs(dx), abs(dy)) 
    x_increment= dx / steps
    y_increment = dy / steps
    x = x1
    y = y1
    for i in range(steps):
        screen.set_at((round (x) , round (y)), GOLD)
        x += x_increment
        y += y_increment
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #clear the screen
        screen.fill(BLACK)
        #draw the line
        draw_line_dda(400,200,400,600)
        draw_line_dda(200,400,600,400)
        draw_line_dda(200,200,600,600)
        draw_line_dda(600,200,200,600)
        draw_line_dda(200,600,600,600)
        draw_line_dda(200,200,600,200)
        draw_line_dda(200,200,200,600)
        draw_line_dda(600,200,600,600)
        draw_line_dda(200,400,400,200)
        draw_line_dda(400,200,600,400)
        draw_line_dda(200,400,400,600)
        draw_line_dda(400,600,600,400)
        #update the display
        pygame.display.flip()
if __name__=='__main__':
    main()
