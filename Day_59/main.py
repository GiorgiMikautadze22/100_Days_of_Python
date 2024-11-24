from flask import Flask, render_template, request
import smtplib
import requests
app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/674f5423f73deab1e9a7")
data = response.json()

def send_email(name, email, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

@app.route('/')
def get_all_posts():
    return render_template("index.html", blogs=data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        send_email(request.form["username"], request.form["email"], request.form["message"])
        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False)

@app.route("/blog/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
