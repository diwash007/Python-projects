from selenium import webdriver

driver_path = "C:\\dev\\geckodriver.exe"
driver = webdriver.Firefox(executable_path=driver_path)

driver.get("https://python.org")

dates = driver.find_elements_by_css_selector(".event-widget time")
events = driver.find_elements_by_css_selector(".event-widget li a")
data = {}
for i in range(len(dates)):
	data[i] = {
				"time" : dates[i].text[5:],
				"name" : events[i].text
			}

print(data)




driver.quit()