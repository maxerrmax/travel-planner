from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/plan", methods=["POST"])
def plan():
    destination = request.form.get("destination")
    days = request.form.get("days")

    return render_template("result.html", destination=destination, days=days)

