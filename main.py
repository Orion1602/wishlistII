from flask import Flask, render_template, request, make_response, redirect, url_for
from models import User, db

app = Flask(__name__)
db.create_all()


@app.route("/", methods=["GET"])
def index():
    user_name = request.cookies.get("name")
    user = db.query(User).filter_by(name=user_name).first()

    return render_template("index.html")


@app.route("/my-wishes", methods=["POST", "GET"])
def getwishes():
    name = request.form.get("user-name")
    wone = request.form.get("user-wone")
    wtwo = request.form.get("user-wtwo")
    wthree = request.form.get("user-wthree")
    wfour = request.form.get("user-wfour")
    wfive = request.form.get("user-wfive")
    wsix = request.form.get("user-wsix")

    user = User(name=name, wone=wone, wtwo=wtwo, wthree=wthree, wfour=wfour, wfive=wfive, wsix=wsix)

    db.add(user)
    db.commit()

    response = make_response(redirect(url_for("showmywishes")))
    response.set_cookie("user_name", name)

    return response


@app.route("/me", methods=["GET"])
def showmywishes():
    user_name = request.cookies.get("name")
    user = db.query(User).filter_by(name=user_name).first()
    return render_template("me.html", user=user)


if __name__ == '__main__':
    app.run()