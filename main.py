import pyautogui
import time
from pynput.mouse import Listener
from pynput import mouse
import numpy as np
import os
import pyscreenshot as ImageGrab
import cv2
import pytesseract


tessPath = r'D:\Tesseract-OCR\tesseract.exe'
fName = 'Image.png'
def screanshot(x1,y1,x2,y2):
    screen = np.array(ImageGrab.grab(bbox=(x1,y1,x2,y2)))
    cv2.imshow('window',cv2.cvtColor(screen,cv2.COLOR_BGR2RGB))
    cv2.imwrite(fName,screen)
    cv2.destroyAllWindows()
    return None

def on_click(x, y, button, pressed):
    if pressed:
        return False

with mouse.Listener(
    on_click=on_click  

    ) as listener:
    listener.join()

x1,y1=pyautogui.position()
print(x1,y1)

with mouse.Listener(
    on_click=on_click  

    ) as listener:
    listener.join()

x2,y2=pyautogui.position()
print(x2,y2)

screanshot(x1,y1,x2,y2)
pytesseract.pytesseract.tesseract_cmd = tessPath
img = cv2.imread(fName)
text = pytesseract.image_to_string(img)
print(text)
os.remove(fName)