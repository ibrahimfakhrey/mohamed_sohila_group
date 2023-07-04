from flask import Flask, render_template, request, redirect
import requests
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

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
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
with app.app_context():
    class User(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True)
        phone = db.Column(db.String(100), unique=True)
        password = db.Column(db.String(100))
        name = db.Column(db.String(1000))
    db.create_all()
class MyModelView(ModelView):
    def is_accessible(self):
            return True

admin = Admin(app)
admin.add_view(MyModelView(User, db.session))
@app.route("/")
def start():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        name=request.form.get("user")
        password=request.form.get("password")
        users=User.query.all()
        for user in users:
            if name ==user.name and password==user.password:
                url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
                response = requests.get(url=url)
                data = response.json()
                temperature_kelvin = data['main']['temp']
                temp_celsius = int(temperature_kelvin) - 272
                date = datetime.date.today()

                return render_template("w.html", temp=temp_celsius, date=date)

        return redirect("/register")







    return render_template("login.html")


@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        name = request.form.get("user")
        password = request.form.get("password")
        phone=request.form.get("phone")
        new_user=User(
            name=name,
            phone=phone,
            password=password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect("/login")
    return render_template("register.html")




if __name__=="__main__":
    app.run(debug=True)