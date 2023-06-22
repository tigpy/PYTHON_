import pygame
import time
import random
 
pygame.init()

# Set the screen size
WIDTH = 500
HEIGHT = 500
 
# Set the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
 
# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set the font and font size
font = pygame.font.SysFont(None, 25)

# Set the snake block size and speed
BLOCK_SIZE = 10
SPEED = 15
 
# Define the function to display the snake on the screen
def snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE])

# Define the main game loop
def gameLoop():
    gameExit = False
    gameOver = False

    # Set the initial position of the snake and the direction
    lead_x = WIDTH/2
    lead_y = HEIGHT/2
    lead_x_change = 0
    lead_y_change = 0
 
    # Create the snake list and the initial length
    snakeList = []
    snakeLength = 1
 
    # Set the position of the food
    randAppleX = round(random.randrange(0, WIDTH-BLOCK_SIZE)/10.0)*10.0
    randAppleY = round(random.randrange(0, HEIGHT-BLOCK_SIZE)/10.0)*10.0
 
    while not gameExit:
        while gameOver == True:
            # Display the game over message and the final score
            screen.fill(WHITE)
            message = font.render("Game over! Press Q to quit or C to play again", True, RED)
            score = font.render("Score: " + str(snakeLength-1), True, BLACK)
            screen.blit(message, [WIDTH/6, HEIGHT/3])
            screen.blit(score, [WIDTH/2, HEIGHT/2])
            pygame.display.update()
 
            # Check for key events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        # Check for key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -BLOCK_SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = BLOCK_SIZE
                    lead_x_change = 0
 
        # Check if the snake goes out of bounds
        if lead_x >= WIDTH or lead_x < 0 or lead_y >= HEIGHT or lead_y < 0:
            gameOver = True
        
        # Move the snake
        lead_x += lead_x_change
        lead_y += lead_y_change
        
        # Draw the background and the food
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED,) [randAppleX,]
