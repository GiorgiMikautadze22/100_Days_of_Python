from flask import Flask, render_template

app = Flask(__name__)

def make_bold_decorator(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function
@app.route("/")
@make_bold_decorator
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=8080)