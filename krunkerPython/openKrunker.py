import webbrowser
import time

from gotToLogin import goToLogin
from gotToUsername import goToName
from typeUserName import typeName
from goToPassword import goToPassword
from typePassword import typePassword
from clickFinalLogin import goToFinalLogin
from exitProfile import exitProfile
from clickFreeKrButton import clickKrButton
from clickSpinButton import clickKrSpin


chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open('krunker.io')



def main():
	goToLogin()
	goToName()
	typeName()
	goToPassword()
	typePassword()
	goToFinalLogin()
	exitProfile()
	clickKrButton()
	time.sleep(20)
	clickKrSpin()

while True:
	main()
	time.sleep(7260)
	

