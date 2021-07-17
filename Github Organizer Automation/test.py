import os
import requests

user = <your_user_name>

# getting gits url
response = requests.get(url=f"https://api.github.com/users/{user}/repos?per_page=60")
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

# deleting from Github
header = {
   	"Accept" : "application/vnd.github.v3+json",
	"Authorization" : "token <your_token_here>"
}
response = requests.get(url="https://api.github.com/users/{user}/repos?per_page=60")
data = response.json()

name_list = [num["name"] for num in data]
name_list.pop(9) # removing unwanted repos
name_list.pop(9)
name_list.pop(29)
name_list.pop(0)

for repo_name in name_list:
	# print(f"https://api.github.com/repos/{user}/{repo_name}")
	response = requests.delete(url=f"https://api.github.com/repos/{user}/{repo_name}", headers=header)
	print(response.content)