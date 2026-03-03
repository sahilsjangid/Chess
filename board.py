import pygame

#pygame setup
size = 720

pygame.init()       #to initialize all the modules from pygame library

screen = pygame.display.set_mode((size, size))
clock = pygame.time.Clock()
running = True
#need clock running for consistancy, else, program will run as fast as it can in a computer, leading to unplayble gameplay.

rect_width = rect_height = size / 8

while running:
    #poll for events
    #use pygame.QUIT to close the program when user click on x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("black") #runs every frame


    #rander your game here


    square_size = 90
    rect_width = square_size
    rect_height = square_size

    for row in range(8):
        for collunm in range(8):
            x = collunm * square_size
            y = row * square_size

            rect = (x, y, rect_width, rect_height)

            if (collunm + row) % 2 == 0:
                pygame.draw.rect(screen, 'white', rect)

    #flip() to new screen
    pygame.display.flip()

    clock.tick(60) #FPS limit

pygame.quit()

