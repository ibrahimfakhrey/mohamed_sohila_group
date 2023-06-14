from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def start():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        name=request.form.get("user")
        password=request.form.get("password")
        if name =="abdullah" and password=="1234":
            return "my secret is that programming is interesting "
        else:
            return "you are not abdullah try again "

    return render_template("login.html")





if __name__=="__main__":
    app.run(debug=True)