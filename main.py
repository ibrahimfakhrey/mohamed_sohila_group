from flask import Flask, render_template, request, redirect

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




if __name__=="__main__":
    app.run(debug=True)