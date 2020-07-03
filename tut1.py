import pygame
x=pygame.init()

#Creating game window
gamewindow =pygame.display.set_mode((1200,500))
pygame.display.set_caption("My First Game")

#Game specific variables
exit_game = False
game_over = False

#Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            exit_game=True
        if event.type == pygame.KEYDOWN:    #if a key is pressed
            if event.key == pygame.K_RIGHT:     #if right arrow key is pressed
                print("You have pressed down arrow key!")

pygame.quit()
quit()