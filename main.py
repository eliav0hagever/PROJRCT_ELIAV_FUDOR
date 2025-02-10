import pygame
from helpers import *
from constants import *
from buttons import *
from classes.Post import Post
from classes.post_image import imagepost




def main():
    # Set up the game display, clock and headline
    pygame.init()
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    # Change the title of the window
    pygame.display.set_caption('INSTANIZ')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    post1 = post_image.imagepost.imagepost("NoaK","Israel","hello im noa ", "Images/noa_kirel.jpg")
    post2 = post_image.imagepost("Crisiano","Portugal","Im the best foball player","Images/ronaldo.jpg")


    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if mouse_in_button(click_post_button,pos):
                    post1.post_image.display()





        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()
