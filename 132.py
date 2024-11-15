from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
import pandas as pd

driver = webdriver.Edge()
# Тут мой путь и браузерный дравер Edge, но можно и по другому. Снизу путь к Excel-файлу
file_path = "C:\\Users\\ylitk\\PycharmProjects\\pythonProject\\microsoft-edge\\Excelfiles\\challenge.xlsx"
df = pd.read_excel(file_path)
# Расширение Pandas, которое считывает Excel-файл
print(df.head())

try:
    driver.get("https://www.rpachallenge.com/")

    for index, row in df.iterrows():
        # Кнопка старт
        start_button = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button")
        start_button.click()
        # Данные с эксель с поиском внутри эксель файла
        first_name = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']")
        last_name = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']")
        email = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']")
        company_name = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']")
        role_in_company = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']")
        address = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']")
        phone_number = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']")
        submit_button = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input")

        # Работа с переменными, которые указаны через XPATH выше
        first_name.send_keys(row['First Name'])
        last_name.send_keys(row['Last Name '])
        email.send_keys(row['Email'])
        company_name.send_keys(row['Company Name'])
        role_in_company.send_keys(row['Role in Company'])
        address.send_keys(row['Address'])
        phone_number.send_keys(row['Phone Number'])

        # Кнопка Сюдмит, что бы началось и продолжало в цикле
        submit_button.click()

finally:
# Браузер держится 60 секунд и закроется (я знаю есть переменные "сервис", исклюзивно для Selenium, но использовать их слабо умею)
    time.sleep(60)
    driver.quit()