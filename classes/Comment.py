import pygame

from constants import *
from helpers import screen
from helpers import read_comment_from_user


class Comment:
    def __init__(self, comment):
        self.comment = comment

    def display(self, index):
        font = pygame.font.SysFont("Verdana", COMMENT_TEXT_SIZE)
        text = font.render(self.comment, True, (0, 0, 0))
        screen.blit(text, [FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + index * COMMENT_LINE_HEIGHT])
