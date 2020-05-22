from pynput.mouse import Button, Controller
import time

mouse = Controller()

def goToLogin():

	#goes to login position

	mouse.position = (-1850, 285)
	time.sleep(12)

	mouse.click(Button.left, 1)
	print('clicked on login')
	time.sleep(0.5)




	

