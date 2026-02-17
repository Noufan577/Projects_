from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_gender(name):
    response = requests.get(
        "https://api.genderize.io",
        params={"name": name}
    ).json()
    return response.get("gender")

def get_age(name):
    response = requests.get(
        "https://api.agify.io",
        params={"name": name}
    ).json()
    return response.get("age")

@app.route("/")
def home():
    return render_template("index2.html")

@app.route("/predict")
def predict():
    name = request.args.get("uname")

    if not name:
        return "Name not provided", 400

    gender = get_gender(name)
    age = get_age(name)

    return render_template(
        "index1.html",
        uname=name,
        gender=gender,
        age=age
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
