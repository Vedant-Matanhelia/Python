import pyautogui
from PIL import ImageGrab
import time


def hit(key):
    pyautogui.keyDown(key)


def is_collide(data):
    for x in range(290, 391):
        for y in range(415, 450):
            if data[x, y] < 100:
                hit('up')
                return
    return


if __name__ == '__main__':
    time.sleep(3)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        process = image.load()
        is_collide(process)

