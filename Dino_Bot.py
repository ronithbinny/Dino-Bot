from PIL import ImageGrab, ImageOps
import pyautogui            
from numpy import *


pyautogui.moveTo(485,750)
pyautogui.click()

pyautogui.moveTo(682,200)
pyautogui.click()
pyautogui.keyDown("space")

box = (263.7,390,333.7,460) # Top conner pos and Bottom conner pos                                                  
sbox = (345,130,360,145)
a = 0
ti = 0

while True:
    image = ImageGrab.grab(box)
    imageSbox = ImageGrab.grab(sbox)
    
    grayimage = ImageOps.grayscale(image)
    grayimageSbox = ImageOps.grayscale(imageSbox)
    
    a = array(grayimage.getcolors())
    b = array(grayimageSbox.getcolors())
    
    print(a.sum(),ti,b.sum())
    ti = ti + 1
       
    if b.sum() == 480 :
        if a.sum() != 5155 :
             pyautogui.keyDown("space")
             #time.sleep(0.1)
    else  :
        if a.sum() != 3600 :
            pyautogui.keyDown("space")                                                                                                                                                                                                                                                                                          
