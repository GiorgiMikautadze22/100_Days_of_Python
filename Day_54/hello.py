from flask import Flask

app = Flask(__name__)

def make_bold_decorator(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function
@app.route("/")
@make_bold_decorator
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True, port=8080)