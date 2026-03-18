import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)

boxes = []
score = 0

spawn_timer = 0
spawn_delay = 800  # ms

fall_speed = 2

running = True

while running:
    screen.fill((20, 20, 20))
    dt = pygame.time.get_ticks()

    # Eevent Listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            for box in boxes[:]:
                x, y, size = box

                if x < mx < x + size and y < my < y + size:
                    boxes.remove(box)
                    score += 1
                    break

    # box spawner
    if pygame.time.get_ticks() - spawn_timer > spawn_delay:
        size = 40
        x = random.randint(0, WIDTH - size)
        boxes.append([x, 0, size])
        spawn_timer = pygame.time.get_ticks()

    # update
    for box in boxes[:]:
        box[1] += fall_speed

        # remove if out of screen
        if box[1] > HEIGHT:
            boxes.remove(box)
            score -= 1

    # Ddraw box
    for box in boxes:
        x, y, size = box
        pygame.draw.rect(screen, (0, 200, 255), (x, y, size, size))

    # scorw
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()