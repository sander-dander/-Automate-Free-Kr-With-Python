from pynput.mouse import Button, Controller
import time

mouse = Controller()



def clickKrButton():

	time.sleep(1)
	mouse.position = (-1732, 386)
	time.sleep(1)
	mouse.click(Button.left, 1)

clickKrButton()


