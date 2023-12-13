from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/write")
def write():
    return render_template("write.html")

@app.route("/forgotpassword")
def forgotpassword():
    return render_template("forgotpassword.html")

if __name__  ==  "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)