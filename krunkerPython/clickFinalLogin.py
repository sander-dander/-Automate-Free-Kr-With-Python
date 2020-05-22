from pynput.mouse import Button, Controller
import time

mouse = Controller()


def goToFinalLogin():

	time.sleep(2)
	mouse.position = (-803, 970)
	time.sleep(1)
	mouse.click(Button.left, 1)
	print('Clciked final login button')


