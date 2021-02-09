import random
from sys import exit
import pygame
from pygame.locals import *
# Global Variables initialization
FPS = 45
SCREEN_WIDTH = 289
SCREEN_HEIGHT = 511
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GROUND_Y = SCREEN_HEIGHT * 0.8
GAME_SPRITES = {}
GAME_AUDIO = {}
PLAYER = './gallery/sprites/bird.png'
PIPE = './gallery/sprites/pipe.png'
BACKGROUND = './gallery/sprites/background.png'


def welcome_screen():
    """Shows welcome images on the screen"""
    player_x = int(SCREEN_WIDTH/5)
    player_y = int((SCREEN_HEIGHT - GAME_SPRITES['player'].get_height())/2)
    message_x = int((SCREEN_WIDTH - GAME_SPRITES['message'].get_width())/2)
    message_y = int(SCREEN_HEIGHT * 0.13)
    base_x = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                exit()

            # If the user presses space or up key, start the game for them
            elif (event.type == KEYDOWN) and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['player'], (player_x, player_y))
                SCREEN.blit(GAME_SPRITES['message'], (message_x, message_y))
                SCREEN.blit(GAME_SPRITES['base'], (base_x, GROUND_Y))
                pygame.display.set_icon(GAME_SPRITES['icon'])
                pygame.display.update()
                FPS_CLOCK.tick(FPS)


def get_random_pipe():
    """
    Generate Two pipes for blitting 1 straight and one rotated
    Bottom
    :return:
    """
    pipe_height = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREEN_HEIGHT / 3
    y2 = offset + random.randrange(0, int(SCREEN_HEIGHT-GAME_SPRITES['base'].get_height()-1.2*offset))
    pipe_x = SCREEN_WIDTH + 10
    y1 = pipe_height - y2 + offset
    pipe = [
        {'x': pipe_x, 'y': -y1},  # For upper pipe
        {'x': pipe_x, 'y': y2},  # For lower pipe
    ]
    return pipe


def is_collide(player_x, player_y, upper_pipes, lower_pipes, ):
    """
    Checks for collision

    :param player_x:
    :param player_y:
    :param upper_pipes:
    :param lower_pipes:
    :return:
    """
    if player_y > GROUND_Y - 25 or player_y < 0:
        GAME_AUDIO['hit'].play()
        return True
    for pipe in upper_pipes:
        pipe_height = GAME_SPRITES['pipe'][0].get_height()
        if (player_y < pipe_height + pipe['y']) and abs(player_x - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_AUDIO['hit'].play()
            return True
    for pipe in lower_pipes:
        if (player_y + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(player_x - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_AUDIO['hit'].play()
            return True
    return False


def main_game():
    global FPS
    score = 0
    player_x = int(SCREEN_WIDTH/5)
    player_y = int(SCREEN_WIDTH/2)
    base_x = 0

    # Create 2 pipes for blitting
    new_pipe_1 = get_random_pipe()
    new_pipe_2 = get_random_pipe()

    # List of upper pipes
    upper_pipes = [
        {'x': SCREEN_WIDTH+200, 'y': new_pipe_1[0]['y']},
        {'x': SCREEN_WIDTH+200+(SCREEN_WIDTH/2), 'y': new_pipe_2[0]['y']}
    ]
    # List of lower pipes
    lower_pipes = [
        {'x': SCREEN_WIDTH + 200, 'y': new_pipe_1[1]['y']},
        {'x': SCREEN_WIDTH + 200 + (SCREEN_WIDTH / 2), 'y': new_pipe_2[1]['y']}
    ]
    pipe_vel_x = -4
    player_vel_y = -9
    player_max_vel_y = 10
    # player_min_vel_y = -8
    player_acc_y = 1
    player_flap_vel = -8  # Velocity by flapping
    player_flapped = False  # Becomes true while flapping
    while True:
        pygame.display.set_icon(GAME_SPRITES['icon'])
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if player_y > 0:
                    player_vel_y = player_flap_vel
                    player_flapped = True
                    GAME_AUDIO['wing'].play()

        crash_test = is_collide(player_x, player_y, upper_pipes, lower_pipes, )
        if crash_test:
            return

        # Check for Score
        player_mid_pos = player_x + GAME_SPRITES['player'].get_width()/2
        for pipe in upper_pipes:
            pipe_mid_pos = pipe['x']+GAME_SPRITES['pipe'][0].get_width()/2
            if pipe_mid_pos <= player_mid_pos < pipe_mid_pos + 4:
                score += 1
                # print(f"Your score is {score}")
                GAME_AUDIO['point'].play()

        if player_vel_y < player_max_vel_y and not player_flapped:
            player_vel_y += player_acc_y

        if player_flapped:
            player_flapped = False
        player_height = GAME_SPRITES['player'].get_height()
        player_y += min(player_vel_y, GROUND_Y - player_y - player_height)

        # move pipes to the left
        for upper_pipe, lower_pipe in zip(upper_pipes, lower_pipes):
            upper_pipe['x'] += pipe_vel_x
            lower_pipe['x'] += pipe_vel_x

        # Add a new pipe when the pipe is about to cross
        if 0 < upper_pipes[0]['x'] < 5:
            new_pipe = get_random_pipe()
            upper_pipes.append(new_pipe[0])
            lower_pipes.append(new_pipe[1])
        # If the pipe is out of screen then remove it
        if upper_pipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upper_pipes.pop(0)
            lower_pipes.pop(0)

        # Blitting of sprites
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for upper_pipe, lower_pipe in zip(upper_pipes, lower_pipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0], (upper_pipe['x'], upper_pipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (lower_pipe['x'], lower_pipe['y']))
        SCREEN.blit(GAME_SPRITES['base'], (base_x, GROUND_Y))
        SCREEN.blit(GAME_SPRITES['player'], (player_x, player_y))
        my_digits = [int(x) for x in list(str(score))]
        width = 0
        for digit in my_digits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        x_offset = (SCREEN_WIDTH - width)/2

        for digit in my_digits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (x_offset, SCREEN_HEIGHT*0.12))
            x_offset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


if __name__ == '__main__':
    # This is the main game
    pygame.init()  # Initialize the game window
    FPS_CLOCK = pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird")
    GAME_SPRITES['numbers'] = (
        pygame.image.load('./gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/9.png').convert_alpha(),
    )
    GAME_SPRITES['message'] = pygame.image.load('./gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('./gallery/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha()
    )
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITES['icon'] = pygame.image.load('./gallery/sprites/icon.png')
    # Game Audio
    GAME_AUDIO['die'] = pygame.mixer.Sound('./gallery/audio/die.wav')
    GAME_AUDIO['hit'] = pygame.mixer.Sound('./gallery/audio/hit.wav')
    GAME_AUDIO['swoosh'] = pygame.mixer.Sound('./gallery/audio/swoosh.wav')
    GAME_AUDIO['wing'] = pygame.mixer.Sound('./gallery/audio/wing.wav')
    GAME_AUDIO['point'] = pygame.mixer.Sound('./gallery/audio/point.wav')
    while True:
        welcome_screen()
        main_game()
