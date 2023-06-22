from flask import Flask, render_template, request, redirect
import requests
import datetime

lat = "30.357519"
lon = "31.204611"
api_key = "3eab6e609ad2c6909fd44c6a6d1a5dac"


url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
response = requests.get(url=url)
data = response.json()
temperature_kelvin = data['main']['temp']
temp_celsius = int(temperature_kelvin) - 272
app=Flask(__name__)

users={
    "mohamed":"0000",
    "ali":"1234",
    "omar":"1122"
}
@app.route("/")
def start():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        name=request.form.get("user")
        password=request.form.get("password")
        for key in users:
            if name ==key:
                if password==users[key]:
                    return "my secret is that programming is interesting "




        return redirect("/register")

    return render_template("login.html")


@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        name = request.form.get("user")
        password = request.form.get("password")
        users[name]=password
        return redirect("/login")
    return render_template("register.html")


@app.route("/weather")
def w():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url=url)
    data = response.json()
    temperature_kelvin = data['main']['temp']
    temp_celsius = int(temperature_kelvin) - 272
    date=datetime.date.today()

    return render_template("w.html",temp=temp_celsius,date=date)

if __name__=="__main__":
    app.run(debug=True)