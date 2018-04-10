from selenium import webdriver
import time
import random
import datetime


# -----------------------
login = "login"
password = "pass"
path = "appfiles\\chromedriver.exe"
# -----------------------


while True:
    try:
        driver = webdriver.Chrome(path)  # Path to Chrome Driver
        dnevnik = driver.get("http://login.dnevnik.ru/login")
        loginBox = driver.find_element_by_name("login")
        passwordBox = driver.find_element_by_name("password")
        time.sleep(random.randint(5, 20))  # Delay between the login page loaded and login entered
        loginBox.send_keys(login)
        time.sleep(random.randint(5, 20))  # Delay between entering password and login
        passwordBox.send_keys(password + "\n")
        time.sleep(random.randint(10, 600))  # Delay between news feed and diary
        buttons = driver.find_elements_by_class_name("_1B6-z")
        buttons[0].click()
        print("[", datetime.datetime.now(), "]", " Login done!")
        time.sleep(random.randint(360, 600))  # Delay between diary and off
        driver.close()
        time.sleep(random.randint(5400, 14400))  # Delay between logins
    except Exception:
        pass
