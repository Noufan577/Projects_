from flask import Flask
from flask import render_template
import requests

def get_gender(name):
    parm={
        "name": name
    }
    response=requests.get(url="https://api.genderize.io",params=parm).json()

    return response["gender"]

def get_age(name):
    parm={
        "name":name
    }
    response=requests.get(url="https://api.agify.io",params=parm).json()

    return response["age"]
    



    

app = Flask(__name__)


@app.route("/")
def home():
    return "<b><h1>Welcome to my predictor</h1></b><br><br><h3>write you name in the url and gooooo!!!!!</h3>"

@app.route("/<name>")
def page(name):
    gender=get_gender(name)
    age=get_age(name)
    return render_template("index.html",uname=name,gender=gender,age=age)


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
    
    




if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)

