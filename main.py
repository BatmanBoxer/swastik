from pynput import keyboard
import pyautogui

billNumber = int(input("Bill Number (RN)- "))
def on_press(key):
    global billNumber
    try:
        print(key)
        if key == keyboard.Key.home:
            print("darwin")
            keyboard.write(f"RN-{billNumber}")
            billNumber = billNumber + 1
    except AttributeError:
            print(f'Special key {key} pressed')


def on_release(key):
    print("-------------------------------------------")
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
