from pynput.mouse import Button, Controller
import time

mouse = Controller()

time.sleep(3)
print(mouse.position)

def exitProfile():

	
	mouse.position = (-455, 479)
	time.sleep(1)
	mouse.click(Button.left, 1)
