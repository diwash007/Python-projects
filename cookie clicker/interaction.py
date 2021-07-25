from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = "C:\\dev\\geckodriver.exe"
driver = webdriver.Firefox(executable_path=driver_path)

# wikipedia data
driver.get("https://en.wikipedia.org/wiki/Main_Page")
number = driver.find_element_by_css_selector("#articlecount a")
print(number.text)

# filling and submitting form
driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
btn = driver.find_element_by_class_name("btn")
fname.send_keys("Hello")
lname.send_keys("World")
email.send_keys("Hello@world.com")
btn.click()

driver.quit()