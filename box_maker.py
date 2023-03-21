import pygame
from random import randint


class Builder:
    def __init__(self, *args):
        self.boxes = []

    def makeboxes(self, surface, current_window_size, *args):
        self.boxes = []
        window_x = current_window_size[0]
        window_y = current_window_size[1]
        for n in range(0, window_x, 30):
            for m in range(0, window_y - 300, 10):
                if (n, m) in args[0]:
                    pass

                else:
                    box = pygame.draw.rect(surface,
                                           color=(100, 0, 200),
                                           rect=pygame.Rect(n, m, 30, 10),
                                           border_radius=2)

                    self.boxes.append(box)
