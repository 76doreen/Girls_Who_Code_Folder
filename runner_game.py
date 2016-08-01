import pygame
from random import *
from block import *
from building1 import *

pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
LAVENDER = (230, 230, 250)
LAVENDER_BLUSH = (255, 240, 245)
MISTY_ROSE = (255, 228, 225)
HONEYDEW = (240, 255, 240)
MINT_CREAM = (245, 255, 250)
AZURE = (240, 255, 255)
ALICE_BLUE = (240, 248, 255)
SALMON = (250, 128, 114)
LIGHT_SALMON = (255, 165, 0)
LIGHT_CORAL = (240, 128, 128)

colors = [BLACK, WHITE, GREEN, BLUE, RED, GREY, LAVENDER, LAVENDER_BLUSH, MISTY_ROSE, HONEYDEW, MINT_CREAM, AZURE, ALICE_BLUE, SALMON, LIGHT_SALMON, LIGHT_CORAL]

clock = pygame.time.Clock()
score = 0
lives = 10

font = pygame.font.SysFont("Clarendon", 25, True, False)
font1 = pygame.font.SysFont("Clarendon", 100, True, False)

make_blocks()

done = False

while not done:
   
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

    picture = pygame.image.load('DonaldTrump.jpg')
    screen.blit(picture, (350, 350))
    
    buildings_list = []

    x_point = 700
    y_point = 0
    width = random.randint(50, 75)
    height = random.randint(100, 500)
    building_color = random.choice(colors)

    building = Building(700 + width, 500 - height, width, 600, random.choice(colors))
    buildings_list.append(building)

    for building in buildings_list:
        building.draw()
        building.move(2)

    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    black_blocks_hit_list = pygame.sprite.spritecollide(player, black_block_list, True)
    green_blocks_hit_list = pygame.sprite.spritecollide(player, green_block_list, True)

    # Move the blocks.
    black_block_list.update()
    green_block_list.update()

    # Check the list of collisions.
    for block in green_blocks_hit_list:
        score += 1
        lives += 0.5

    for block in black_blocks_hit_list:
        lives -= 1

    score_text = font.render("Score: " +str(score), True, BLACK)
    lives_text = font.render("Lives: "+ str(lives), True, BLACK)

    if lives <= 0:    
        screen.fill(RED)
        text = font1.render("GAME OVER.", True, WHITE)
        screen.blit(text, [120, 250])
    else:
        screen.fill(AZURE)

    if score >= 15 and score < 30:
        screen.fill(LAVENDER)

    if score >=30 and score <45:
        screen.fill(LIGHT_CORAL)


    if score >=45:
        screen.fill(MISTY_ROSE)

    screen.blit(score_text, [500, 50])
    screen.blit(lives_text, [50, 50])

    all_sprites_list.draw(screen)

    pygame.display.flip()

    if lives <= 0: 
        pygame.time.delay(1000)
        done = True

    clock.tick(60)

pygame.quit()
exit()
