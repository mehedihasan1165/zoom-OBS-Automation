import pyautogui
import time
import os
import schedule

print('\nWelcome to Zoom and OBS Automation')
print('\nEnter the following details regarding the meeting to set it up...')
print('Read the README.md file before going any further')
print('\nYou can exit this program using ( Ctrl+c ) at any time\n')
meet_id = input('Enter Meeting ID: ')
password = input('Enter Meeting password: ')
meet_time = input('Enter everyday meeting time in 24hour format (eg: "22:45" for 10:45pm): ')
total_meet = input('How long will the meeting last for ?(Answer in minutes eg:60 for 1 hour): ')
total_meet = int(total_meet) * 60
meeting_time = str(meet_time)


def obs_recording_start():
    pyautogui.press('win', interval=1.5)
    pyautogui.write('obs')
    pyautogui.press('enter', interval=1.5)
    time.sleep(15)
    x, y = pyautogui.locateCenterOnScreen('images\\startRecording.png', confidence=0.9)
    time.sleep(2)
    pyautogui.click(x, y)
    time.sleep(2)


def obs_recording_stop():
    x, y = pyautogui.locateCenterOnScreen('images\\stopRecording.png', confidence=0.9)
    time.sleep(2)
    pyautogui.click(x, y)
    time.sleep(5)
    os.system('TASKKILL /F /IM obs64.exe')


def zoom():
    pyautogui.press('win', interval=1.5)
    pyautogui.write('zoom')
    pyautogui.press('enter', interval=1.5)
    time.sleep(15)
    x, y = pyautogui.locateCenterOnScreen('images\\join.png', confidence=0.9)
    time.sleep(2)
    pyautogui.click(x, y)
    pyautogui.press('enter', interval=5)
    pyautogui.write(meet_id)
    pyautogui.press('enter', interval=5)
    pyautogui.write(password)
    pyautogui.press('enter', interval=10)
    time.sleep(total_meet)
    os.system('TASKKILL /F /IM Zoom.exe')
    time.sleep(0.5)


def automation():
    obs_recording_start()
    zoom()
    obs_recording_stop()


schedule.every().day.at(meet_time).do(automation)
print('\nscheduling every day at ', meet_time)

while True:
    schedule.run_pending()
    time.sleep(1)
