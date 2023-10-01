from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from playsound import playsound, PlaysoundException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome()
reserv_url = 'https://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do#'
login_url = "https://www.letskorail.com/korail/com/login.do"
driver.get(login_url)

input("Please Login, then press Enter key")


def play_tada():
    try:
        playsound('tada.mp3')
    except PlaysoundException:
        print("ERROR: tada.mp3를 재생하지 못했습니다.")


try:
    element = driver.find_element(By.CLASS_NAME, "log_nm")
    driver.get(reserv_url)

except NoSuchElementException:
    print("Please Login, First")
    exit(-1)


while True:
    try:
        print("Select Flavor")
        driver.find_element(By.CLASS_NAME, "btn_drop").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "myDropdown").click()
        time.sleep(0.5)
        print("Try Reservation")
        driver.find_element(By.CLASS_NAME, "btn_buynow").click()
        time.sleep(0.5)
    except NoSuchElementException:
        print("There is no Flavor")
        driver.get(reserv_url)

    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("Reservation Success")
        play_tada()
        break
    except NoAlertPresentException :
        element = driver.find_element(By.CLASS_NAME, "btn_blue_ang")
        if element:
            print("Retry")
            element.click()
            time.sleep(0.5)

    #     element = driver.find_element(By.CLASS_NAME, "btn_blue_ang")
    #     if element:
    #         print("Retry")
    #         element.click()
    #         time.sleep(0.5)
    # except NoSuchElementException:
    #     element = driver.find_element(By.CLASS_NAME, "btn_red_ang")
    #     if element:
    #         print("Reservation Success")
    #         play_tada()
    #         break
    #     else:
    #         driver.get(reserv_url)
