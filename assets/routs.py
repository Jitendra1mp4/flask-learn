from assets import app
from flask import render_template, request
import assets.moduls as modul


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
       result = modul.saveData()
       return result
    return render_template("homepage.html")


@app.route("/users")
def users_page():
    users = modul.getUsers()
    if users == [] : 
        return "<h1> We got nothing</h1>"
    return render_template("users_page.html", users=users)
