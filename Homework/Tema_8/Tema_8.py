import time

from selenium import webdriver
from selenium.webdriver.common.by import By

''' Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri '''



chrome = webdriver.Chrome()

#By.ID
chrome.get('https://phptravels.net/')
chrome.maximize_window()
chrome.find_element(By.ID, 'autocomplete').send_keys('Sibiu')
time.sleep(2)
chrome.find_element(By.ID, 'autocomplete2').send_keys('Barcelona')
time.sleep(2)
chrome.find_element(By.ID, 'departure').click()
time.sleep(2)

#By.LINK_TEXT
chrome.find_element(By.LINK_TEXT, 'services').click()
time.sleep(5)