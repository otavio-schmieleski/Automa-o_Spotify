from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui
import time
from pathlib import Path
import json
ROOT_FOLDER = Path(__file__).parent / 'dados.json'

#informacao do ususario
email = input('Informe seu e-mail  ')
password = input('Informe sua senha  ')

navegador = webdriver.Chrome()
navegador.get('https://open.spotify.com/')
time.sleep(2)
navegador.find_element('xpath','//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]').click()
time.sleep(2)
navegador.find_element('xpath','//*[@id="login-username"]').send_keys(f"{email}")
navegador.find_element('xpath','//*[@id="login-password"]').send_keys(f"{password}")
navegador.find_element('xpath','//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/div/label/span[1]/span').click()
navegador.find_element('xpath','//*[@id="login-button"]/span[1]').click()
time.sleep(5)
navegador.find_element('xpath','//*[@id="main"]/div/div[2]/div[2]/nav/div[2]/div[1]/div[2]/div[4]/div/div/div/div[2]/ul/div/div[2]/li[2]/div/div[1]').click()
time.sleep(1)
navegador.find_element('xpath','//*[@id="main"]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[4]/div/div/div/div/div/button/span').click()
time.sleep(2)
#pyautogui.click(x=1258,y=743)
#pyautogui.click(x=1294, y=617)

input('Precione Enter para encerrar a automação')
navegador.quit()
