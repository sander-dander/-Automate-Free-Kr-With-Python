from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def typeName():
	time.sleep(5)
	for char in "your krunker username": 

		keyboard.press(char)
		keyboard.release(char)
		time.sleep(0.5)
