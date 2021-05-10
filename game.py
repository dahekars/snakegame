import pygame
import time 
import random

# active Pygame 
pygame.init()

#colur 
red = (255,0,0)
white = (255, 255, 255)
black = (0,0, 0)
orange = (255,165, 0)

#dimantions
width, height = 600, 400

#display
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("test snake")

clock = pygame.time.Clock()
 
snake_size = 10
snake_speed = 15

message = pygame.font.SysFont("ubuntu", 10)

scores = pygame.font.SysFont("ubuntu", 15)

#define
def scores_display(score):
    text = scores.render("Score: " + str(score), True, orange)
    game_display.blit(text, [0, 0])

def draw_snake(snake_size, snake_pixel):
    for pixel in snake_pixel:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])

def run_game():
    game_over = False
    game_close = False
    
    #starting Position
    x = width/2
    y = height/2
    
    #starting speed
    x_speed = 0
    y_speed = 0
    
    #snake starting condition
    snake_pixel = []
    snake_length = 1

    #tarage discrip
    tarage_x = round(random.randrange(0, width - snake_size)/10.0)*10
    tarage_y = round(random.randrange(0, height - snake_size)/10.0)*10
    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message = message.render(f"Game over \n Score: {snake_length - 1}", True, red)
            game_display.blit(game_over_message, [width/2, height/2])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            #key actions
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size
        #limits of boundry 
        if x >= width or y >= height or x < 0 or y < 0:
            game_close = True
        
        x += x_speed
        y += y_speed

        # starting dispaly
        game_display.fill(black)
        pygame.draw.rect(game_display, orange, [tarage_x, tarage_y, snake_size, snake_size])

        snake_pixel.append([x, y])

        # checking for snake size
        if len(snake_pixel)> snake_length:
            del snake_pixel[0]
        
        for pixel in snake_pixel[:-1]:
            if pixel == [x,y]:
                game_over = True
        
        draw_snake(snake_size, snake_pixel)
        scores_display(snake_length-1)

        pygame.display.update()

        if x == tarage_x and y == tarage_y:
            tarage_x = round(random.randrange(0, width - snake_size)/10.0)*10
            tarage_y = round(random.randrange(0, height - snake_size)/10.0)*10
            snake_length += 1

        clock.tick(snake_speed)
    
    pygame.QUIT
    quit()

run_game()
