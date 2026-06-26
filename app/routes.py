from flask import Blueprint, render_template, request
from app.services.ai_service import generate_plan
from app.database import (
    save_itinerary,
    get_all_itineraries,
    get_itinerary_by_id
)
import markdown

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")


@main.route("/plan", methods=["POST"])
def plan():

    destination = request.form["destination"]
    days = request.form["days"]
    preferences = request.form["Preferences"]

    days = int(days) if days else 0
    destination = destination.strip()
    preferences = preferences.strip() if preferences else ""

    plan_raw = generate_plan(destination, days, preferences)
    plan = markdown.markdown(plan_raw)
    save_itinerary(destination, days, preferences, plan)

    return render_template(
        "result.html",
        destination=destination,
        days=days,
        plan=plan
    )

@main.route("/history")
def history():

    itineraries = get_all_itineraries()

    return render_template(
        "history.html",
        itineraries=itineraries
    )

@main.route("/trip/<int:id>")
def trip(id):

    itinerary = get_itinerary_by_id(id)

    if itinerary is None:
        return "Trip not found", 404

    return render_template(
        "result.html",
        destination=itinerary[0],
        days=itinerary[1],
        preferences= itinerary[2],
        plan=itinerary[3]
    )