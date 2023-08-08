from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def homepage():
    return render_template("homepage.html")


@app.route("/users")
def users_page():
    users = [
        {"id": 1, "name": "Jitendra Kumar", "phone": "914355335", "address": "Raipur"},
        {"id": 2, "name": "Fake Gurus", "phone": "787554844", "address": "Rajim"},
        {"id": 3, "name": "John Cally", "phone": "954871554", "address": "Navapara"},
        {"id": 4, "name": "Sita Kumar", "phone": "684548754", "address": "Abhanpur"},
    ]
    return render_template("users_page.html", users=users)
