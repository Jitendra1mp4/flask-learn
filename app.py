# setting some environment variables 
#cmd :  set FLASK_APP=app.py in windows and 
#cmd : export FLASK_APP = app.py in linux
# To turn the debug mod on we need to run following command 
#cmd : set FLASK_DEBUG=1


from flask import Flask #,jsonify,request, render_template

app = Flask(__name__)

# decorator in python 
@app.route("/") #where root of our website
def home() : 
        return "<h1>I t it would not works</h1>"


# this is called as dynamic route
@app.route("/about/<username>")
def about(username) :
        return (f"Hello {username}!")

 
