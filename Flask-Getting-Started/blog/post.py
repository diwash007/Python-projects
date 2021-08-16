import requests


class Post:
	def __init__(self):
		blog_url = "https://api.npoint.io/7617aece62c07fee8ada"
		data = requests.get(blog_url)
		self.posts = data.json()