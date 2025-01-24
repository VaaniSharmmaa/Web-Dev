from flask import Flask ,render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/") #decorator
def home():
    return render_template('index.html')

@app.route("/login", methods= ["POST", "GET"]) #POST se we share data
def login():
    if request.method =="POST":
        user = request.form("nm")
        return redirect(url_for("user", usr = user))
    else:
        return render_template("login.html")
    

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"
if __name__ == "__main__":
    app.run()