from flask import Flask ,jsonify,request, render_template

app = Flask(__name__)

@app.route("/")
def home() : 
        return "<h1>I think i would works</h1>"
