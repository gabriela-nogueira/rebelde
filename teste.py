from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tkinter import messagebox
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.eventim.com.br/event/rbd-allianz-parque-16563626/")
#driver.get("https://www.eventim.com.br/event/wu-tang-clan-arena-open-air-16479044/?affiliate=PL5")

time.sleep(3)

while True:
    print("Tentando encontrar o elemento.")
    try:
        element = driver.find_element(By.CLASS_NAME, 'js-cc-submit-btn')
        break
    except:
        time.sleep(3)
        driver.refresh()
    

messagebox.showinfo('Encontrou')