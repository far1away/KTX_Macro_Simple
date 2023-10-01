from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time,os 
from playsound import playsound, PlaysoundException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
import chromedriver_autoinstaller_fix

def play_tada():
    try:
        playsound('tada.mp3')
    except PlaysoundException:
        print("ERROR: tada.mp3를 재생하지 못했습니다.")

# Check if chrome driver is installed or not
chrome_ver = chromedriver_autoinstaller_fix.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chrom driver is insatlled: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
    chromedriver_autoinstaller_fix.install(True)


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome()

reserv_url = 'https://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do#'
login_url = "https://www.letskorail.com/korail/com/login.do"
preset_url = "https://www.letskorail.com/korail/com/mypage/preset/preset_list.do"

driver.get(login_url)
input("Please Login, then press Enter key")

try:
    element = driver.find_element(By.CLASS_NAME, "log_nm")
    driver.get(preset_url)

except NoSuchElementException:
    print("Please Login, First")
    exit(-1)

input("Please Create Preset, then press Enter key ( If you already have a preset, Just Press Enter Key )")


y_n = input ("Do you need manual input? Y or N : ")

if y_n.lower() == "y":
    start= input("Please Input Departure Station : ")
    end= input("Please Input Arrival station : ")
    year= input("Please Input Year : ")
    month= input("Please Input Month : ")
    month = month.zfill(2)
    date= input("Please Input Date : ")
    date = date.zfill(2)
    hour= input("Please Input Time(Hour Base) : ")
    hour = hour.zfill(2)
else :
    print("Use a previously entered preset.")


#document.getElementById("start").value="부산"

driver.get(reserv_url)

while True:
    try:
        print("Select Flavor")
        driver.find_element(By.CLASS_NAME, "btn_drop").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "myDropdown").click()
        time.sleep(0.5)

        if y_n == "y":
            print("Set Target Preset Manually")
            driver.find_element(By.ID, "start").clear()
            driver.find_element(By.ID, "start").send_keys(start)
            driver.find_element(By.ID, "get").clear()
            driver.find_element(By.ID, "get").send_keys(end)
            select = Select(driver.find_element(By.ID, "s_year"))
            select.select_by_value(year)
            select = Select (driver.find_element(By.ID, "s_month"))
            select.select_by_value(month)
            select = Select (driver.find_element(By.ID, "s_day"))
            select.select_by_value(date)
            select = Select ( driver.find_element(By.ID, "s_hour"))
            select.select_by_value(hour)
        print("Try Reservation")

        driver.find_element(By.CLASS_NAME, "btn_buynow").click()
        time.sleep(0.5)
        if y_n == "y":
            try : 
                alert = driver.switch_to.alert
                if "20분" in alert.text :
                    print("Reservation Success")
                    play_tada()
                    break
                else:
                    alert.accept()
                time.sleep(0.5)
            except NoAlertPresentException :
                time.sleep(0.1)

    except NoSuchElementException:
        print("There is no Flavor")
        driver.get(reserv_url)

        continue

    try:
        alert = driver.switch_to.alert
        if "20분" in alert.text :
            print("Reservation Success")
            play_tada()
            alert.accept()
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
