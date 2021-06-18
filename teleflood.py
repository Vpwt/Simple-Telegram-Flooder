import webbrowser
import time
import keyboard

url = input("Input Weblink Of Telegram User or Group >> ")
msg = input("Enter A Message You Want To Flood >> ")
webbrowser.open(url, new=1, autoraise=True)
time.sleep(20)

while True:
    keyboard.write(msg)
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(0.5)
