import pygame

from constants import *
from helpers import screen, from_text_to_array,center_text
import Post

class Text_post(Post):
    def __init__(self,username, location,description,text,text_color,backround_color):
        super().__init__(username, location, description)
        self.text_arry = from_text_to_array(text)
        self.text_color = text_color
        self.background_color = backround_color
    def display(self):
        pygame.draw.rect(screen,self.background_color,pygame.Rect(POST_X_POS,POST_Y_POS,POST_WIDTH,POST_HEIGHT))
        counter = 0
        for text in self.text_arry:
            screen.fill(self.background_color)
            font=pygame.font.SysFont('chalkduster.ttf',TEXT_POST_FONT_SIZE,bold= False )
            text = font.render(self.text_arry,True,self.text_color)
            text_position = center_text(len(self.text_arry),text,counter)
            counter+=1
            screen.blit(text,text_position)

        super().display()