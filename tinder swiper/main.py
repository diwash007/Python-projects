from selenium import webdriver
import time

driver_path = "C:\\dev\\geckodriver.exe"
driver = webdriver.Firefox(executable_path=driver_path)

# loading tinder
driver.get("https://www.tinder.com")
time.sleep(10)

# clicking on login
login = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
login.click()
time.sleep(7)

# clicking on login with Google
google = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[1]/div/button")
google.click()
time.sleep(10)

# getting windows info & switching to Google popup
windows = driver.window_handles
driver.switch_to.window(windows[-1])

# inputting email
user = driver.find_element_by_xpath('//*[@id="identifierId"]')
user.send_keys("freequotesforyoumyfriend@gmail.com")

# proceeding next
nextBtn = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
nextBtn.click()

# Google signin didnt work .. so leaving it