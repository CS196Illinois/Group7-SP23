from flask import Flask, redirect, url_for

app = Flask(__name__)
def home():
    return "Hello! This is a sample home page"
@app.route("/<name>")
def user(name):
    return "Hello {name}!"
@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()