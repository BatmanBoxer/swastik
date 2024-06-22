import keyboard
import pyautogui

billnb = int(input("bill nb start: "))
agent = input("Enter agent name: ")

def on_key_event(event):
    global billnb  # This allows the function to modify the global variable
    if event.event_type == 'down':
        if event.name == ',' and event.modifiers == {'ctrl'}:
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
        elif event.name == '.' and event.modifiers == {'ctrl'}:
            pyautogui.press("enter")
            pyautogui.typewrite(agent)
            pyautogui.press("enter")
        elif event.name == '/' and event.modifiers == {'ctrl'}:
            pyautogui.press("enter")
            pyautogui.typewrite(f"RN-{billnb}")
            pyautogui.press("enter")
            billnb += 1
mero name darwin ho
print("Press ',' to press Enter four times.")
print("Press '.' to press Enter, type agent name, and press Enter.")
print("Press '/' to press Enter, type RN-billnb, press Enter, and increment billnb.")
keyboard.hook(on_key_event)

# Keep the program running indefinitely
keyboard.wait("[")
