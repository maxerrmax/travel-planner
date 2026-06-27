from flask import Blueprint, render_template, request
from app.services.ai_service import generate_plan
from app.services.image_service import get_destination_image
from app.utils.validator import validate_trip
from app.database import (
    save_itinerary,
    get_all_itineraries,
    get_itinerary_by_id
)
import json
import logging

logger = logging.getLogger(__name__)

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")


@main.route("/plan", methods=["POST"])
def plan():

    destination = request.form["destination"]
    days = request.form["days"]
    preferences = request.form["Preferences"]
    budget = request.form["budget"]

    days = int(days) if days else 0
    destination = destination.strip()
    budget = budget.strip() if budget else ""
    preferences = preferences.strip() if preferences else ""

    try:
        trip = generate_plan(destination, days, preferences, budget)

        image_url = get_destination_image(destination)

        save_itinerary(
            destination,
            days,
            preferences,
            budget,
            image_url,
            json.dumps(trip)
        )

    except Exception:
        return render_template(
            "error.html",
            message="We couldn't generate your itinerary right now. Please try again in a few moments."
        )

    logger.info("Trip generated successfully.")

    return render_template(
        "result.html",
        destination=destination,
        days=days,
        trip=trip,
        image_url=image_url
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
        preferences=itinerary[2],
        budget=itinerary[3],
        image_url=itinerary[4],
        trip=json.loads(itinerary[5]) 
    )