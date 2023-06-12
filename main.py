from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def start():
    return render_template("login.html")

@app.route("/mohamed")
def mohamed():
    return "sohila"
@app.route("/mohaned")
def m():
    return"mohanad"
if __name__=="__main__":
    app.run(debug=True)