'''import pygame
x = pygame.init()

#FOR WINDOW CREATION
gameWindow = pygame.display.set_mode((1200,500))

#NAME OF WINDOW
pygame.display.set_caption("SAPY GAME-1")

#VARIABLES
exit_game=False
game_over=False

#GAME not end till end
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("pressed right")

pygame.quit()
quit()'''

import pygame
import random
import os

#for game sound


pygame.mixer.init()

pygame.init()

screen_height=1200
screen_width=600

#window creation
gameWindow = pygame.display.set_mode((screen_height,screen_width))

#background img
img = pygame.image.load("snake_and_skull.jpg")
img = pygame.transform.scale(img, (1200, 1200)).convert_alpha()

#NAME OF WINDOW
pygame.display.set_caption("SAPY SNAKES GAME-1")
pygame.display.update()

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
maroon= (128,0,0)

clock = pygame.time.Clock()

# for score display
font = pygame.font.SysFont(None, 70)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    # to update screen
    gameWindow.blit(screen_text, [x, y])

def plotsnake(gameWindow, color, snlist, snake_size):
    for x, y in snlist:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])

def home():
    exit_game=False
    pygame.mixer.music.load('start.mp3')
    pygame.mixer.music.play(-1)
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(img,(0,0))

        text_screen("WELCOME TO SNAKES GAME",green, 260,200)
        text_screen("PRESS 'ENTER' TO START", green, 300, 295)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    loop()

        pygame.display.update()
        clock.tick(60)

#GAME not end till end
def loop():

    # VARIABLES
    exit_game = False
    game_over = False

    snake_x = 55
    snake_y = 55
    snake_size = 20

    velocity_x = 5
    velocity_y = 5

    score = 0

    food_x = random.randint(50, screen_width / 4)
    food_y = random.randint(50, screen_height / 4)

    fps = 15
    snlist = []
    snlength = 1

    pygame.mixer.music.load('medium.mp3')
    pygame.mixer.music.play(-1) #-1 to playit on loop

    if(not os.path.exists("game.txt")):
        with open("game.txt", "w") as f:
            f.write("0")

    with open("game.txt","r") as f:
        highscore=f.read()


    while not exit_game:

        if game_over:
            gameWindow.fill(black)
            with open("game.txt", "w") as f:
                f.write(str(highscore))
            text_screen("GAME OVER!!!",red, 400,100)
            text_screen("PRESS ENTER TO CONTINUE...", red, 220, 190)
            text_screen("YOUR SCORE: " + str(score), white, 380, 300)
            text_screen("HIGHSCORE: " + str(highscore), white, 390, 400)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        pygame.mixer.music.load('start.mp3')
                        pygame.mixer.music.play(-1)
                        home()


        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x=10
                        velocity_y=0

                    if event.key == pygame.K_LEFT:
                        velocity_x=-10
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y=-10
                        velocity_x=0

                    if event.key == pygame.K_DOWN:
                        velocity_y=+10
                        velocity_x=0

                    #cheatcode
                    if event.key==pygame.K_q:
                        score+=10

            snake_x+=velocity_x
            snake_y+=velocity_y

            if abs(snake_x-food_x)<8  and (snake_y-food_y)<8:
                score+=10
                food_x = random.randint(20, screen_height / 2)
                food_y = random.randint(20, screen_width / 2)
                snlength+=2
                if score > int(highscore):
                    highscore=score


            gameWindow.fill(green)
            text_screen("YOUR SCORE: " + str(score + 10), maroon, 30, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            #pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])


            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snlist.append(head)

            if len(snlist)>snlength:
                del snlist[0]

            if snake_x<0 or snake_x>screen_height or snake_y<0 or snake_y>screen_width:
                game_over=True
                pygame.mixer.music.load('end.mp3')
                pygame.mixer.music.play(-1)

            if head in snlist[:-1]: #if the head collapses with any element except last element i.e head itself
                game_over=True
                pygame.mixer.music.load('end.mp3')
                pygame.mixer.music.play(-1)

            plotsnake(gameWindow, black, snlist, snake_size)  # for increasing snake size

        clock.tick(fps)  #frame per second

        pygame.display.update()

    pygame.quit()
    quit()
home()
loop()