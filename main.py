import math

import pygame, sys, random

pygame.init()

size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)

x = [200]
y = [200]

copy_x = [200]
copy_y = [200]

food_x = random.randint(0, 1000)
food_y = random.randint(0, 1000)

eaten = False


def update_pos():
    for j in range(len(x)):
        if j == 0:
            pass
        else:
            x[j] = copy_x[j-1]

    for j in range(len(y)):
        if j == 0:
            pass
        else:
            x[j] = copy_y[j-1]


def food_pos_update():
    return [random.randint(0, 1000), random.randint(0, 1000)]


def border_check():
    if x[0] < 0 or x[0] > 1000:
        return True
    elif y[0] < 0 or y[0] > 1000:
        return True
    else:
        return False


def eaten_check():
    if math.dist([x[0], y[0]], [food_x, food_y]) <= math.sqrt(1800):
        return True


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

        if e.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                x[0] -= 30
            if keys[pygame.K_RIGHT]:
                x[0] += 30
            if keys[pygame.K_DOWN]:
                y[0] += 30
            if keys[pygame.K_UP]:
                y[0] -= 30
            if keys[pygame.K_e]:
                # Only for Testing
                eaten = True
            update_pos()
            copy_x = x
            copy_y = y

    screen.fill((0, 0, 0))

    if border_check():
        # Add a Death Window or Retry Window
        sys.exit()

    if eaten_check():
        x.append(x[len(x)-1]+35)
        y.append(y[len(y)-1])
        copy_x.append(x[len(x)-1] + 35)
        y.append(y[len(y)-1])
        eaten = True

    for i in range(len(x)):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x[i], y[i], 30, 30))

    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(food_x, food_y, 30, 30))
    if eaten:
        food_x, food_y = food_pos_update()
        eaten = False

    pygame.display.flip()
