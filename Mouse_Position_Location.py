import pyautogui

n = 0
while n < 10 :
    print(pyautogui.position())
    time.sleep(5)
    n = n + 1
