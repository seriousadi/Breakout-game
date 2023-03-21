import pygame
from pygame._sdl2.touch import *
from box_maker import Builder

# pygame setup
pygame.init()
screen = pygame.display.set_mode((300, 500))
clock = pygame.time.Clock()
running = True
window_size = pygame.display.get_window_size()
box_maker = Builder()
x = 100
y = 300
xn = 5
yn = 5

# lines on borders
line1 = pygame.draw.line(screen, color=(255, 0, 0), start_pos=(0, 0), end_pos=(300, 0), width=40)
line2 = pygame.draw.line(screen, color=(255, 0, 0), start_pos=(0, 0), end_pos=(0, 500), width=4)
line3 = pygame.draw.line(screen, color=(255, 0, 0), start_pos=(300, 500), end_pos=(300, 0), width=4)
line4 = pygame.draw.line(screen, color=(255, 0, 0), start_pos=(300, 500), end_pos=(0, 500), width=4)
lines = []
for n in [line1, line2, line3, line4]:
    lines.append(n)
box_to_remove = []
while running:
    screen.fill("white")
    box_maker.makeboxes(screen, window_size,box_to_remove)
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    strikerX = pygame.mouse.get_pos()[0]  # Taking mouse x co-ordinate to move the striker
    # RENDER YOUR GAME HERE

    striker = pygame.draw.rect(surface=screen,
                               color=(255, 192, 203),
                               rect=pygame.Rect(strikerX, 400, 90, 10),
                               border_radius=2)
    ball = pygame.draw.rect(screen, color=(255, 0, 0), rect=pygame.Rect(x, y, 10, 10), border_radius=3)

    if ball.colliderect(striker):
        yn = -5
    elif ball.collideobjects(box_maker.boxes):
        yn = 5
        collided_with_box = (ball.collideobjects(box_maker.boxes).x, ball.collideobjects(box_maker.boxes).y)
        if collided_with_box not in box_to_remove:
            box_to_remove.append(collided_with_box)
            print(box_to_remove)

    if ball.x > 300 or ball.x < 0:
        xn = xn * -1
    elif ball.y > 500 or ball.y < 0:
        yn = yn * -1
    x += xn
    y += yn
    # flip() the display to put your work on screen

    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60
pygame.quit()
