# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((300, 500))
clock = pygame.time.Clock()
running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    strikerX = pygame.mouse.get_pos()[0]  # Taking mouse x co-ordinate to move the striker
    # RENDER YOUR GAME HERE
    striker = pygame.draw.rect(surface=screen,
                               color=(255, 0, 0),
                               rect=pygame.Rect(strikerX, 400, 90, 10),
                               border_radius=2)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 60

pygame.quit()
