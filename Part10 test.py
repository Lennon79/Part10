#Lennon Hudson
import pygame

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, WHITE, [1+x,y,10,10], 0)
    # Legs
    pygame.draw.line(screen, WHITE ,[5+x,17+y], [10+x,27+y], 2)
    pygame.draw.line(screen, WHITE, [5+x,17+y], [x,27+y], 2)
    # Body
    pygame.draw.line(screen, RED, [5+x,17+y], [5+x,7+y], 2)
    # Arms
    pygame.draw.line(screen, RED, [5+x,7+y], [9+x,17+y], 2)
    pygame.draw.line(screen, RED, [5+x,7+y], [1+x,17+y], 2)
    #To do this we need the smallest x value (95 in this function) and the smallest y value (83 in this function).
    #Subtract all x and y values in the function by these amounts. Now our figure is drawn next to the origin instead in the middle of our screen.
    #Now our figure is drawn next to the origin instead in the middle of our screen.
    #Now add the x that is passed to the function all x-values, and the y value passed to the function to all y
    #values. This will draw the shape relative to whatever point is passed to the function.

'''
def draw_stick_figure(screen,x,y):
    # Head
    pygame.draw.ellipse(screen, WHITE, [96,83,10,10], 0)
    # Legs
    pygame.draw.line(screen, WHITE, [100,100], [105,110], 2)
    pygame.draw.line(screen, WHITE, [100,100], [95,110], 2)
    # Body
    pygame.draw.line(screen, RED, [100,100], [100,90], 2)
    # Arms
    pygame.draw.line(screen, RED, [100,90], [104,100], 2)
    pygame.draw.line(screen, RED, [100,90], [96,100], 2)
'''
'''
def draw_snowman(screen, x, y):
    pygame.draw.ellipse(screen, WHITE, [35+x, y, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [23+x, 20+y, 50, 50])
    pygame.draw.ellipse(screen, WHITE, [x, 65+y, 100, 100])
'''

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    '''
    draw_snowman(screen, 400, 10)
    draw_snowman(screen, 400, 210)
    draw_snowman(screen, 400, 410)
    '''
    '''
    draw_stick_figure(screen, 50, 50)#not actually drawn at 50,50.
    #This is because we didn't use the x and y values passed to our function to draw shapes
    #we want the figure drawn as close to the origin (0,0) as close as possible
    '''
    draw_stick_figure(screen, 50, 150)
    draw_stick_figure(screen, 100, 150)
    draw_stick_figure(screen, 350, 250)
    draw_stick_figure(screen, 90, 390)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()