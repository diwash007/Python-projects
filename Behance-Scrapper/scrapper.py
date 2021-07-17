import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import shutil
  
#url of the page we want to scrape
url = "https://www.behance.net/diwash"
  
# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Edge('./msedgedriver') 
driver.get(url) 
  
# this is just to ensure that the page is loaded
time.sleep(10) 
  
page = driver.page_source
  
# this renders the JS code and stores all
# of the information in static HTML code.
  
# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(page, 'html.parser')
links = soup.find_all('img', class_='js-cover-image')

num = 1
for link in links:
	img_url = link.get('src')
	filename = 'pic'+str(num)+'.jpg'
	r = requests.get(img_url, stream = True)

		# Check if the image was retrieved successfully
	if r.status_code == 200:
	    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
	    r.raw.decode_content = True
	    
	    # Open a local file with wb ( write binary ) permission.
	    with open(filename,'wb') as f:
	        shutil.copyfileobj(r.raw, f)
	        
	    print('Image sucessfully Downloaded: ',filename)
	    num+=1
	else:
	    print('Image Couldn\'t be retreived')

  
driver.close() # closing the webdriver