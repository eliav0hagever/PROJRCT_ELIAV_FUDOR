import pygame
from helpers import *
from constants import *
from buttons import *
from classes.Post import Post
from classes.post_image import Imagepost
from classes.text_post import Text_post
from classes.Comment import *


def main():
    pygame.init()
    pygame.display.set_caption('INSTANIZ')
    clock = pygame.time.Clock()

    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

    post1 = Imagepost("NoaK", "Israel", "hello im noa ", "Images/noa_kirel.jpg")
    post2 = Imagepost("Crisiano", "Portugal", "Im the best football player", "Images/ronaldo.jpg")
    post3 = Text_post(" floyd", "o block", "special cat", "SHUMACHERRRRRR", BLACK, WHITE)
    post4=Imagepost("igal", "Israel", "hi nro ", "Images/ddd.jpg")

    # Variable to keep track of the current post index
    current_post_index = 0

    posts = [post1, post2,post3,post4]

    running = True
    while running:
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        # Display the current post
        posts[current_post_index].display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(f"Mouse clicked at: {pos}")
                if mouse_in_button(click_post_button, pos):
                    print("Button clicked")
                    # Move to the next post
                    current_post_index = (current_post_index + 1) % len(posts)
                elif mouse_in_button(like_button, pos):
                    posts[current_post_index].like_counter += 1
                elif mouse_in_button(comment_button, pos):
                    comment_text = read_comment_from_user(screen)
                    if comment_text:
                        comment = Comment(comment_text)
                        posts[current_post_index].add_comment(comment)
        for index, comment in enumerate(posts[current_post_index].comments):
            comment.display(index)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
