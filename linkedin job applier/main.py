from selenium import webdriver

PASSWORD = ""
USER = ""

driver_path = "C:\\dev\\geckodriver.exe"
driver = webdriver.Firefox(executable_path=driver_path)

data = driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=104630404&keywords=python%20developer&location=Nepal&position=1&pageNum=0")

signin = driver.find_element_by_css_selector(".nav .nav__button-secondary")
signin.click()

email = driver.find_element_by_name("session_key")
email.send_keys(USER)
password = driver.find_element_by_name("session_password")
password.send_keys(PASSWORD)

button = driver.find_element_by_css_selector(".login__form_action_container button")
button.click()