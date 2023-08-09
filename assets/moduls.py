from flask import request
from assets import mysql


def saveData():
    status = "Successfully Inserted Data"
    try:
        uname = request.form.get("uname")
        passw = request.form.get("passw")
        cur = mysql.connection.cursor()
        qurry = "insert into users (name,phone) VALUES (%s,%s);"
        cur.execute(qurry, (uname, passw))
        mysql.connection.commit()
    except:
        status = "faild to save data"
    finally:
        cur.close()
    return status


def getUsers():
    cur = mysql.connection.cursor()
    listItems = cur.execute("select * from users")
    if listItems == 0:
        return []
    users = cur.fetchall()
    cur.close()
    return users
