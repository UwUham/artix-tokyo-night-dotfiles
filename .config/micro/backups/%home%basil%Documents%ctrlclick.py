from pymouse import PyMouseEvent
import time

def clicc():
    clicc = True
    time.sleep(0.1)
    clicc = False

class checkClick(PyMouseEvent):

    def __init__(self):
        PyMouseEvent.__init__(self)

    def click(self, x, y, button, press):
        if button == 1:
            if press:
                print("clicc!")

C = checkClick()
C.run()

def show(key):
  
    print(key)
    if key == "Key.ctrl" and press:
        pyautogui.click(button.'right')
  
  
# Collect all event until released
with Listener(on_press = show) as listener:   
    listener.join()

