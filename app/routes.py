from flask import Blueprint, render_template, request
from app.services.ai_service import generate_plan
import markdown

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/plan", methods=["POST"])
def plan():
    days = request.form.get("days")
    days = int(days) if days else 0
    destination = request.form.get("destination")
    preferences = request.form.get("preferences")
    destination = destination.strip()
    preferences = preferences.strip() if preferences else ""

    plan_raw = generate_plan(destination, days, preferences)
    plan = markdown.markdown(plan_raw)

    return render_template(
        "result.html",
        destination=destination,
        days=days,
        plan=plan
    )

