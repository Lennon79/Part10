#Lennon Hudson
#cat and mouse
import pygame

def draw_mouse(screen, x, y):
    pygame.draw.ellipse(screen, PINK, [x, y, 20, 20])
    pygame.draw.ellipse(screen, DARK_GREY, [x, y+5, 60, 30])
    pygame.draw.ellipse(screen, PINK, [x+20, y, 20, 20])
    pygame.draw.ellipse(screen, BLACK, [x+10, y+15, 5, 5])
    pygame.draw.ellipse(screen, PINK, [x-5, y+18, 10, 10])
    pygame.draw.line(screen, PINK, [x+60, y+20], [x+80, y+20], 3)

x=300
y=300

x_speed = 0
y_speed = 0

x_coord = 10
y_coord = 10

def draw_cat(screen, x, y):#move with keyboard
    pygame.draw.ellipse(screen, ORANGE, [x, y+70, 100, 50])#body
    pygame.draw.ellipse(screen, ORANGE, [x-15, y+45, 50, 50])#head
    pygame.draw.ellipse(screen, ORANGE, [x + 15, y + 100, 15, 25])#leg1
    pygame.draw.ellipse(screen, ORANGE, [x + 35, y + 105, 15, 25])#leg2
    pygame.draw.ellipse(screen, ORANGE, [x + 55, y + 100, 15, 25])#leg3
    pygame.draw.ellipse(screen, ORANGE, [x + 75, y + 100, 15, 25])#leg4
    pygame.draw.line(screen, ORANGE, [x + 90, y + 90], [x + 120, y + 50], 8)#tail
    pygame.draw.ellipse(screen, ORANGE, [x + 10, y + 35, 15, 25])  # ear1
    pygame.draw.ellipse(screen, ORANGE, [x-10 , y + 38, 15, 25])  # ear2
    pygame.draw.ellipse(screen, BLACK, [x + 15, y + 60, 5, 5])  # eye
    pygame.draw.ellipse(screen, BLACK, [x , y + 60, 5, 5])  # eye2
    pygame.draw.line(screen, BLACK, [x + 9, y + 70], [x + 12, y + 80], 3)  # mouth1
    pygame.draw.line(screen, BLACK, [x + 10, y + 70], [x + 4, y + 80], 3)  # mouth2
    pygame.draw.ellipse(screen, BLACK, [x+6, y + 66, 8, 8])  # nose


# Define some colors
BLACK = (0, 0, 0)
WHITE = (222, 212, 184)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT_BROWN = (176, 124, 40)
DARK_BROWN = (148, 98, 16)
GREY = (184, 177, 158)
PINK = (237, 166, 221)
DARK_GREY = (79, 75, 78)
ORANGE = (255, 162, 0)

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
    # --- Game logic should go here
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    x_coord += x_speed
    y_coord += y_speed
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(LIGHT_BROWN)

    # --- Drawing code should go here
    #drawing room:
    pygame.draw.rect(screen, DARK_BROWN, [0, 70, 700, 80])
    pygame.draw.rect(screen, GREY, [0, 0, 700, 70])
    pygame.draw.rect(screen, WHITE, [0, 0, 700, 20])
    pygame.draw.rect(screen, DARK_BROWN, [0, 100, 75, 500])
    pygame.draw.rect(screen, GREY, [0, 70, 25, 500])
    #drawing mouse:
    draw_mouse(screen, x, y)
    pygame.mouse.set_visible(False)
    #drawing cat:
    draw_cat(screen, x_coord, y_coord)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()