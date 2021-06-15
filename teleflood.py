import webbrowser
import time
import keyboard

weblink = input(print("input weblink of telegram user/group\t"))
webbrowser.open(weblink, new=1, autoraise=True)
time.sleep(100)

msg = input(print("enter a message you want to flood\t"))

while True:
    keyboard.write(msg)
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(2)
