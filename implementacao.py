import pyautogui
from PIL import ImageGrab
import time

pyautogui.FAILSAFE = False

posicao_pixel_verde = (2340, 1015)
posicao_player = (630,461)

def pixel_eh_verde(x, y):
    regiao = ImageGrab.grab(bbox=(x - 5, y - 5, x + 5, y + 5))
    cor_pixel = regiao.getpixel((5, 5))
    return cor_pixel == (0, 219, 132)

while True:
    if pixel_eh_verde(*posicao_pixel_verde):
        pyautogui.click(posicao_pixel_verde)
        print("Clicou na posição do pixel verde.")
        pyautogui.click(posicao_player)
    
    time.sleep(0.1)
