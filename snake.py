import pygame,random
import os

pygame.mixer.pre_init()
pygame.mixer.init()
pygame.init()

#Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

#Screen width and height
screen_width= 900
screen_height= 600
gamewindow =pygame.display.set_mode((screen_width,screen_height))

#Background image
bgimg = pygame.image.load("snake.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

#Creating game window and updating title
clock = pygame.time.Clock()
pygame.display.set_caption("Snakes")
pygame.display.update()

font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])

def plot_snake(gamewindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        gamewindow.fill((230,220,229))
        text_screen("Welcome to Snakes", black, 250, 300)
        text_screen("Press space bar to play", black, 225, 350)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('bgmusicwav.wav'))
                    game_loop()
        pygame.display.update()
        clock.tick(60)

#Game loop
def game_loop():

    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 450
    snake_y = 300

    score = 0

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    food_size = 20

    snake_size = 20
    velocity_x = 0
    velocity_y = 0
    fps = 30

    snake_list = []
    snake_length = 1

    #Check if high score file exists
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("highscore.txt", 'r') as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            pygame.mixer.Channel(0).pause()
            gamewindow.fill(white)
            text_screen("Game Over! Press enter to continue", red, 100, 250)
            text_screen("                   Your Score:" + str(score), red, 100, 300)
            with open('highscore.txt','w') as f:
                f.write(str(hiscore))

            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.stop()
                        welcome()

        else:
                for event in pygame.event.get():
                    if event.type is pygame.QUIT:
                        exit_game=True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            velocity_x=4
                            velocity_y=0

                        if event.key == pygame.K_LEFT:
                            velocity_x=-4
                            velocity_y=0

                        if event.key == pygame.K_DOWN:
                            velocity_y=4
                            velocity_x=0

                        if event.key == pygame.K_UP:
                            velocity_y=-4
                            velocity_x=0

                        if event.key == pygame.K_q:
                            score+=20

                snake_x = snake_x + velocity_x
                snake_y = snake_y + velocity_y

                if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('Beep_Shortwav.wav'))
                    score+=10
                    food_x = random.randint(20, screen_width / 2)
                    food_y = random.randint(35, screen_height / 2)
                    snake_length+=5
                    if score>int(hiscore):
                        hiscore = score

                gamewindow.fill(white)
                gamewindow.blit(bgimg,(0,0))
                text_screen("Score: " + str(score) + "          High Score: " + str(hiscore), red, 5, 5)
                # pygame.draw.rect(gamewindow, black, [snake_x, snake_y, snake_size, snake_size])

                head = []
                head.append(snake_x)
                head.append(snake_y)#head(snake_x,snake_y)
                snake_list.append(head)
                plot_snake(gamewindow, black, snake_list, snake_size)

                if len(snake_list)>snake_length:
                    del snake_list[0]

                if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                    # Start playing background music
                    pygame.mixer.music.load('Battle_Cry_High_Pitch.mp3')
                    pygame.mixer.music.play()
                    game_over=True
                    # print("Game Over")

                if head in snake_list[:-1]:
                    pygame.mixer.music.load('Battle_Cry_High_Pitch.mp3')
                    pygame.mixer.music.play()
                    game_over=True
                pygame.draw.rect(gamewindow, red, [food_x, food_y, food_size, food_size])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
game_loop()
