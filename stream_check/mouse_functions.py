import pyautogui
import time


class Mouse_functions:


	def open_menu(self):
		pyautogui.moveTo(1660, 90)
		time.sleep(0.5)
		pyautogui.click()
		time.sleep(0.5)

	def open_audio_video(self):
		pyautogui.moveTo(980, 360)
		time.sleep(0.5)
		pyautogui.click()
		time.sleep(0.5)

	def p480_check(self):
		pyautogui.moveTo(950, 660)
		time.sleep(0.5)
		pyautogui.click()
		time.sleep(0.5)
		pyautogui.moveTo(1500, 530)
		pyautogui.click()
		time.sleep(5)

	def p720_check(self):
		pyautogui.moveTo(950, 620)
		time.sleep(0.5)
		pyautogui.click()
		time.sleep(0.5)
		pyautogui.moveTo(1500, 530)
		pyautogui.click()
		time.sleep(5)

	def p1080_check(self):
		pyautogui.moveTo(950, 580)
		time.sleep(0.5)
		pyautogui.click()
		time.sleep(0.5)
		pyautogui.moveTo(1500, 530)
		pyautogui.click()
		time.sleep(5)
                