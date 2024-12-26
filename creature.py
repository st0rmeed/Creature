import os
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((300, 300))
creature = pygame.image.load(os.path.join('data', 'creature.png'))

speed_x = 0
speed_y = 0

speed = 10

left, right, down, up = False, False, False, False

while True:
    screen.fill((255, 255, 255))
    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_UP:
                up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_DOWN:
                down = False
            if event.key == pygame.K_UP:
                up = False

    if right:
        speed_x += speed
    if left:
        speed_x -= speed
    if down:
        speed_y += speed
    if up:
        speed_y -= speed

    screen.blit(creature, (speed_x, speed_y))
    pygame.display.update()
