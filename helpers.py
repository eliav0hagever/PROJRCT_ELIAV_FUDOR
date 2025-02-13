import pygame

from constants import *

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)


def from_text_to_array(text):
    """
    the function get text and break it into sentences that fits the screen, in
    case the text too long to for one line
    :param text: string
        text to show on screen
    :return: list of sentences
    """
    text_array = []
    text_to_edit = text
    if len(text) > 20:
        while not (len(text_to_edit) <= 0):
            if len(text_to_edit) < LINE_MAX_LENGTH:
                text_array.append(text_to_edit)
                text_to_edit = ""
            else:
                temp = text_to_edit[0: LINE_MAX_LENGTH]
                text_to_edit = text_to_edit[LINE_MAX_LENGTH:]
                while not (temp[-1] == ' ') and not (temp[-1] == ','):
                    text_to_edit = temp[-1] + text_to_edit
                    temp_len = int(len(temp))
                    temp = temp[0: temp_len - 1]
                text_array.append(temp)
    else:
        text_array.append(text)
    return text_array


def mouse_in_button(button, mouse_pos):
    """
    The function get button and mouse press position on screen and return True
    if mouse click on button
    :param button: Button object
        button on screen
    :param mouse_pos: tuple
        the x and y position of the mouse cursor
    :return: boolean
        True if mouse click on button, else False
    """
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True


def draw_comment_text_box():
    """

    """
    input_box = pygame.Rect(VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS, 300, 30)

    pygame.draw.rect(screen, GREY, input_box)
    pygame.draw.rect(screen, WHITE, input_box.inflate(-2, -2))
    pygame.draw.rect(screen, BLACK, input_box, 2)

    pygame.display.update()

    return input_box


def read_comment_from_user(screen):
    """

    """
    pygame.font.init()
    font = pygame.font.SysFont('chalkduster.ttf', 24, bold=False)

    input_box = draw_comment_text_box()
    new_comment = ""
    active = True

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    new_comment = new_comment[:-1]
                else:
                    new_comment += event.unicode

        pygame.draw.rect(screen, WHITE, input_box.inflate(-2, -2))
        pygame.draw.rect(screen, BLACK, input_box, 2)

        input_text = font.render(new_comment, True, (0, 0, 0))
        screen.blit(input_text, (input_box.x + 5, input_box.y + 5))

        pygame.display.update()

    return new_comment.strip() if new_comment.strip() else None


def center_text(num_of_rows, text_to_display, row_number):
    """
    center a sentence on screen
    :param num_of_rows: int
        number of sentences on screen
    :param text_to_display: string
        sentence to center
    :param row_number: int
        sentence row number in total text
    :return: tuple
        position of centered text
    """
    horizontal_margin = \
        (POST_HEIGHT - num_of_rows * TEXT_POST_FONT_SIZE) // 2
    # Get the text object size (height and width)
    text_rect = text_to_display.get_rect()
    # Center the text to the center of X axis
    text_rect.x = ((POST_WIDTH - text_rect.width) // 2) + 20
    # Center the text to the center of the post on Y axis
    text_rect.y = (POST_Y_POS + horizontal_margin +
                   row_number * TEXT_POST_FONT_SIZE)
    return text_rect
