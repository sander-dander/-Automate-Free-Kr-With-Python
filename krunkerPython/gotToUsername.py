from pynput.mouse import Button, Controller
import time

mouse = Controller()


def goToName():

	#click on username

	mouse.position = (-1075, 825)
	time.sleep(1)
	mouse.click(Button.left, 2)
	print('clicked on username')

