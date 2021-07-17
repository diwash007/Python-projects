import os
import requests

# getting gits url
response = requests.get(url="https://api.github.com/users/diwash007/repos?per_page=60")
data = response.json()

url_list = [num["clone_url"] for num in data]

url_list.pop(9) # removing unwanted repos
url_list.pop(9)
# cloning
for url in url_list:
	os.system(f"git clone {url}")

# deleting all .git folders
hmm = os.listdir(os.getcwd())
for h in hmm:
	os.system(f"del {h} /A:H")