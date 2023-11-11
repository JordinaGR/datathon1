from selenium import webdriver
import time
import pyautogui as auto
from bs4 import BeautifulSoup as bs
import requests

url = "https://www.google.es/maps/dir/Abrera,+08630,+Barcelona/Facultat+de+Matem%C3%A0tiques+i+Estad%C3%ADstica+-+UPC,+Campus+Diagonal+Sud,+Carrer+de+Pau+Gargallo,+Barcelona/@41.4020286,1.8547837,10.7z/data=!3m1!5s0x12a4985823db5775:0x5c5423949d2895e8!4m14!4m13!1m5!1m1!1s0x12a48bf1cde435a9:0x2f0a4b86d1b0dd78!2m2!1d1.9017802!2d41.5175266!1m5!1m1!1s0x12a498582711d819:0xa37cf84e2892cb6f!2m2!1d2.1158245!2d41.3834784!3e3?entry=ttu"

driver = webdriver.Firefox()

driver.get(url)
time.sleep(1.5)
auto.moveTo(745, 1009)
auto.click()

auto.hotkey('winleft', 'left')

time.sleep(2)

auto.moveTo(165, 204)
auto.click()
auto.hotkey('ctrl', 'a')
auto.typewrite('tarragona')

auto.moveTo(164, 254)
auto.click()
auto.hotkey('ctrl', 'a')
auto.typewrite('facultat de matemàtiques i estadistica')

auto.moveTo(387, 246) #botó cerca
auto.click()

auto.moveTo(197, 136) #botó transport privat
auto.click()

time.sleep(2)
auto.moveTo(275, 499)
auto.click()
auto.moveTo(95, 217)
auto.mouseDown()
auto.moveTo(182, 219)
auto.hotkey('ctrl', 'c')
auto.mouseUp()
auto.moveTo(1358, 149)
auto.click()
auto.hotkey('ctrl', 'v')

time.sleep(1)

auto.moveTo(99,135)
auto.click()

time.sleep(.5)

auto.moveTo(249, 135) #boto transport public
auto.click()
time.sleep(.5)
auto.moveTo(391, 524)
auto.click()
time.sleep(1)

auto.moveTo(232, 220) 
auto.mouseDown()
auto.moveTo(325, 220)
auto.hotkey('ctrl', 'c')
auto.mouseUp()
time.sleep(.5)

auto.moveTo(1358, 149)
auto.click()
time.sleep(.5)

auto.write('-')
auto.moveTo(1358, 149)
auto.click()
auto.hotkey('ctrl', 'v')
time.sleep(.5)

auto.moveTo(1358, 149)
auto.click()
time.sleep(.5)
auto.press('enter')

auto.moveTo(100, 134)
auto.click()
