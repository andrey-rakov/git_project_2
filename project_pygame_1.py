import pygame
import random


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


size = width, height = 400, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Падающие круги')
clock = pygame.time.Clock()
running = True
colors_list = []
coordinate_list = []
radius = 10
v = 100
fps = 60
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            colors_list.append(get_random_color())
            coordinate_list.append(list(event.pos))
    screen.fill(pygame.Color('black'))
    for i in range(len(coordinate_list)):
        pygame.draw.circle(screen, colors_list[i], (coordinate_list[i][0],
                                                    int(coordinate_list[i][1])), radius)
        if coordinate_list[i][1] >= height - radius:
            coordinate_list[i][1] = height - radius
        else:
            coordinate_list[i][1] += v / fps
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()