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
    um = request.form.get("user-message")

    user = User(name=name, wone=wone, wtwo=wtwo, wthree=wthree, wfour=wfour, wfive=wfive, wsix=wsix, um=um)

    db.add(user)
    db.commit()

    response = make_response(redirect(url_for("thank_you")))
    response.set_cookie("user_name", name)

    return response


@app.route("/thankyou", methods=["GET"])
def thank_you():
    return render_template("thanks.html")


@app.route("/users", methods=["GET"])
def all_users():
    users = db.query(User).all()

    return render_template("users.html", users=users)


@app.route("/user/<user_id>", methods=["GET"])
def user_details(user_id):
    user = db.query(User).get(int(user_id))  # .get() can help you query by the ID

    return render_template("user_details.html", user=user)


if __name__ == '__main__':
    app.run()