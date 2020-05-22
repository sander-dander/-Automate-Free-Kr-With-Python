from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def typePassword():
	time.sleep(5)
	for char in "your krunker password": 

		keyboard.press(char)
		keyboard.release(char)
		time.sleep(0.5)


