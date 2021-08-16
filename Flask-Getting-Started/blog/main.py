from flask import Flask, render_template
from post import Post


app = Flask(__name__)
blog_object = Post()

@app.route('/')
def home():
    return render_template("index.html", posts=blog_object.posts)

@app.route('/post/<blog_id>')
def blog(blog_id):
	return render_template('post.html', post=blog_object.posts[int(blog_id)])


if __name__ == "__main__":
    app.run(debug=True)
