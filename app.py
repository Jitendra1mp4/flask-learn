from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "test"

mysql = MySQL(app)


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        uname = request.form.get('uname')
        passw = request.form.get('passw')
        cur = mysql.connection.cursor()
        qurry = "insert into users (name,phone) VALUES (%s,%s);"
        print(uname, passw)
        print(qurry)
        res = cur.execute(qurry, (uname, passw))
        print("res ", res)
        mysql.connection.commit()
        cur.close()
        return "<h1>Successfully Inserted Data</h1>"
    return render_template("homepage.html")


@app.route("/users")
def users_page():
    cur = mysql.connection.cursor()
    listItems = cur.execute("select * from users")
    if listItems > 0:
        users = cur.fetchall()
        cur.close()
        return render_template("users_page.html", users=users)
    return "<h1> We got nothing</h1>"
