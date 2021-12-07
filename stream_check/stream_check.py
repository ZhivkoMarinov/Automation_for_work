import webbrowser
import pyautogui
import time
import datetime
from mouse_functions import Mouse_functions

#enter valid browser path
browser = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s" #default chrome path for windows10

#browser = '/usr/bin/google-chrome' #default chrome path for ubuntu 20.04

webbrowser.get(browser)

#links to check
urls = ['www.google.com', 'www.amazon.com']

#minutes, which you want to start auto-check. Value in range(0, 59)
x = 12
y = 42

mouse = Mouse_functions()

def mouse_move():
        time.sleep(6)                
                
        mouse.open_menu()                
                
        mouse.open_audio_video()                
                
        mouse.p480_check()                
                
        mouse.open_menu()                
                
        mouse.open_audio_video()                
                
        mouse.p720_check()                
                
        mouse.open_menu()                
                
        mouse.open_audio_video()                
        
        mouse.p1080_check()
                
        pyautogui.hotkey('ctrl', 'w')
                
        return

while True:
    if datetime.datetime.now().minute == x or datetime.datetime.now().minute == y:
        status = pyautogui.confirm(text='Start Automatic 7Mojos Stream Test? \nThe test is mouse related, \nso please dont move your mouse during the test.',
        title='7Mojos Stream Test', buttons=['Yes', 'No'])

        if status == 'Yes':

            for url in urls:
                webbrowser.open(url)
                mouse_move()
                
            pyautogui.alert(text="STREAM TEST COMPLETE. \nDon't forget to send Skype message!", title='7Mojos Stream Test', button='OK')
            time.sleep(60)
    else:
        if datetime.datetime.now().minute > x and datetime.datetime.now().minute < y:
            next_check_time = y - datetime.datetime.now().minute
            print(f"Time to next check: {next_check_time} minutes")
        else:
            if datetime.datetime.now().minute > x and datetime.datetime.now().minute < 60:
                next_check_time = x + (60 - datetime.datetime.now().minute)
                print(f"Time to next check: {next_check_time} minutes")
            else:
                next_check_time = x - datetime.datetime.now().minute
                print(f"Time to next check: {next_check_time} minutes")
        time.sleep(60)

