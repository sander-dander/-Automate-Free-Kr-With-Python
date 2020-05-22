from pynput.mouse import Button, Controller
import time

mouse = Controller()



def clickKrSpin():

	time.sleep(15)
	mouse.position = (-944, 737)
	time.sleep(1)
	mouse.click(Button.left, 1)

clickKrSpin()


