from pynput.mouse import Button, Controller
import time

mouse = Controller()

time.sleep(5)
print(mouse.position)

def goToPassword(): 

	#click on username
	mouse.position = (-1028, 889)
	time.sleep(1)
	mouse.click(Button.left, 2)
	print('clicked on password')