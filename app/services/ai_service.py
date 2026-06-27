from openai import OpenAI
import os
import json


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_plan(destination, days, preferences, budget):
    if not destination or not days:
        return "Error: missing input data"
    try:
        days = int(days)
    except:
        return "Error: days must be a number"
         
    prompt = f"""
        You are an expert travel planner.

        Create a {days}-day itinerary for {destination}.

        Traveler preferences:
        - Interests: {preferences}
        - Budget: {budget}

        Return ONLY valid JSON.
        Do not include Markdown.
        Do not include explanations.
        Do not wrap the JSON inside ```
        For each day, include a "summary" field with 2–3 sentences describing the goal and atmosphere of that day before listing the activities.
        For each activity include a short summary of it (what there is to see, how to get there, information about it, etc.)
        For each meal include information about the restaurant (where it is located, how close it is to the activity, type of restaurant, etc.)
        Bear in mind the price and preferences restrictions..
        If you feel like there is enough time you may add more than one activity (morning, afternoon or evening).

        Use exactly this schema:

        {{
            "title": "string",
            "overview": "string",
            "days": [
                {{
                    "day": 1,
                    "summary": "2-3 sentences describing the goal and atmosphere of the day",
                    "morning": [
                        {{"activity": "name of the activity", "summary": "what there is to see, how to get there, useful info"}}
                    ],
                    "lunch": [
                        {{"activity": "name of the restaurant", "summary": "location, type of food, price range, proximity to morning activity"}}
                    ],
                    "afternoon": [
                        {{"activity": "name of the activity", "summary": "what there is to see, how to get there, useful info"}}
                    ],
                    "dinner": [
                        {{"activity": "name of the restaurant", "summary": "location, type of food, price range, proximity to afternoon activity"}}
                    ],
                    "evening": [
                        {{"activity": "name of the activity", "summary": "what there is to see, how to get there, useful info"}}
                    ]
                }}
            ],
            "tips": [
                "tip 1",
                "tip 2"
            ]
        }}
        """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )     
        return json.loads(response.choices[0].message.content)

    except Exception as e:
        return f"AI error: {str(e)}"
