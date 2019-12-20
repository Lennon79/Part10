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
    #Mouse position
    pos = pygame.mouse.get_pos()#The following command gets the (x,y) position of the mouse, returning a tuple containing these values:
    x = pos[0]
    y = pos[1]
    #To use the x and y values from the tuple, we need to add the following two lines of code:

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
#Now that we have the coordinates, pass them to our draw function in order to place the stick figure where the mouse cursor is:
    draw_stick_figure(screen, x, y)
    pygame.mouse.set_visible(False)#Makes the mouse cursor invisible

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()