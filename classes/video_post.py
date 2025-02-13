import pygame
import cv2
import numpy as np

from constants import *
from helpers import screen
from classes.Post import Post

import cv2
import pygame


class VideoPost(Post):
    def __init__(self, username, location, description, video_path):
        super().__init__(username, location, description)
        self.cap = cv2.VideoCapture(video_path)  # Load video
        self.is_playing = False  # Play only when this post is active

    def display(self):
        """
        Show the video only if this post is active.
        """
        if not self.is_playing:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart video
            self.is_playing = True

        if self.cap.isOpened():
            ret, frame = self.cap.read()  # Read next frame

            if ret:
                # Resize frame to fit post area
                new_width, new_height = 313, 295
                frame = cv2.resize(frame, (new_width, new_height))

                # Convert BGR (OpenCV) to RGB (Pygame)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Rotate and flip to match Pygame format
                frame = np.rot90(frame)
                frame = np.flipud(frame)

                # Convert to Pygame surface
                frame_surface = pygame.surfarray.make_surface(frame)

                # Display video on screen
                screen.blit(frame_surface, (POST_X_POS, POST_Y_POS))
            else:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart if video ends

        super().display()  # Show username, likes, etc.
