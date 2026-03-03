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
    rect_a1 = (0, 0, rect_width, rect_height)
    rect_a3 = (180, 0, rect_width, rect_height)
    rect_a5 = (360, 0, rect_width, rect_height)
    rect_a7 = (540, 0, rect_width, rect_height)
    rect_b2 = (90, 90, rect_width, rect_height)
    rect_b4 = (270, 90, rect_width, rect_height)
    rect_b6 = (450, 90, rect_width, rect_height)
    rect_b8 = (630, 90, rect_width, rect_height)
    rect_c1 = (0, 180, rect_width, rect_height)
    rect_c3 = (180, 180, rect_width, rect_height)
    rect_c5 = (360, 180, rect_width, rect_height)
    rect_c7 = (540, 180, rect_width, rect_height)
    rect_d2 = (90, 270, rect_width, rect_height)
    rect_d4 = (270, 270, rect_width, rect_height)
    rect_d6 = (450, 270, rect_width, rect_height)
    rect_d8 = (630, 270, rect_width, rect_height)
    rect_e1 = (0, 360, rect_width, rect_height)
    rect_e3 = (180, 360, rect_width, rect_height)
    rect_e5 = (360, 360, rect_width, rect_height)
    rect_e7 = (540, 360, rect_width, rect_height)
    rect_f2 = (90, 450, rect_width, rect_height)
    rect_f4 = (270, 450, rect_width, rect_height)
    rect_f6 = (450, 450, rect_width, rect_height)
    rect_f8 = (630, 450, rect_width, rect_height)
    rect_g1 = (0, 540, rect_width, rect_height)
    rect_g3 = (180, 540, rect_width, rect_height)
    rect_g5 = (360, 540, rect_width, rect_height)
    rect_g7 = (540, 540, rect_width, rect_height)
    rect_h2 = (90, 630, rect_width, rect_height)
    rect_h4 = (270, 630, rect_width, rect_height)
    rect_h6 = (450, 630, rect_width, rect_height)
    rect_h8 = (630, 630, rect_width, rect_height)
    
    pygame.draw.rect(screen, 'white', rect_a1)
    pygame.draw.rect(screen, 'white', rect_a3)
    pygame.draw.rect(screen, 'white', rect_a5)
    pygame.draw.rect(screen, 'white', rect_a7)
    pygame.draw.rect(screen, 'white', rect_b2)
    pygame.draw.rect(screen, 'white', rect_b4)
    pygame.draw.rect(screen, 'white', rect_b6)
    pygame.draw.rect(screen, 'white', rect_b8)
    pygame.draw.rect(screen, 'white', rect_c1)
    pygame.draw.rect(screen, 'white', rect_c3)
    pygame.draw.rect(screen, 'white', rect_c5)
    pygame.draw.rect(screen, 'white', rect_c7)
    pygame.draw.rect(screen, 'white', rect_d2)
    pygame.draw.rect(screen, 'white', rect_d4)
    pygame.draw.rect(screen, 'white', rect_d6)
    pygame.draw.rect(screen, 'white', rect_d8)
    pygame.draw.rect(screen, 'white', rect_e1)
    pygame.draw.rect(screen, 'white', rect_e3)
    pygame.draw.rect(screen, 'white', rect_e5)
    pygame.draw.rect(screen, 'white', rect_e7)
    pygame.draw.rect(screen, 'white', rect_f2)
    pygame.draw.rect(screen, 'white', rect_f4)
    pygame.draw.rect(screen, 'white', rect_f6)
    pygame.draw.rect(screen, 'white', rect_f8)
    pygame.draw.rect(screen, 'white', rect_g1)
    pygame.draw.rect(screen, 'white', rect_g3)
    pygame.draw.rect(screen, 'white', rect_g5)
    pygame.draw.rect(screen, 'white', rect_g7)
    pygame.draw.rect(screen, 'white', rect_h2)
    pygame.draw.rect(screen, 'white', rect_h4)
    pygame.draw.rect(screen, 'white', rect_h6)
    pygame.draw.rect(screen, 'white', rect_h8)
    

    #flip() to new screen
    pygame.display.flip()

    clock.tick(60) #FPS limit

pygame.quit()

