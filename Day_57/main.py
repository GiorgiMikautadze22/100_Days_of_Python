from flask import Flask, render_template
import requests
app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
data = response.json()

@app.route('/')
def home():
    return render_template("index.html", data=data)

@app.route('/blog/<int:id>')
def get_blog(id):
    blog = data[id - 1]
    return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
