from flask import Flask, render_template
import requests
app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/674f5423f73deab1e9a7")
data = response.json()

@app.route('/')
def get_all_posts():
    return render_template("index.html", blogs=data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route("/blog/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
