import pyautogui as pg
import pyperclip
import time

position = pg.position()
print(position)


pg.moveTo(x=456,y=87,duration=3) # form pos
# pg.typewrite(‘youtube’, 0.1)

pg.click(x=456,y=87,duration=1)

time.sleep(10) # 10 seconds

pg.typewrite('a.png')

pg.press('enter')
# pyautogui.typewrite(‘a.png’)

pg.click(x=171,y=87,duration=1)


pg.click(x=171,y=87,duration=1)

pg.click(x=171,y=87,duration=1)

pg.click(x=171,y=87,duration=1)

pg.click(x=171,y=87,duration=1)

# pg.typewrite(‘excel’, 0.1)


# Point(x=1253, y=455)