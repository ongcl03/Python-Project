import pyautogui, time


text = input("Enter the text you want to send : ")
loop_number = int(input("Enter how many times you want to send the text : "))
time_to_wait = int(input("Enter time to wait to send the text in seconds : "))

time.sleep(time_to_wait)


for i in range(loop_number):
    
    try:
        pyautogui.typewrite(text)
        pyautogui.press("Enter")

    except Exception:
        pass
