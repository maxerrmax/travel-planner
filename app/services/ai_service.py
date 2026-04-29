from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_plan(destination, days, preferences):
    if not destination or not days:
        return "Error: missing input data"
    try:
        days = int(days)
    except:
        return "Error: days must be a number"
    prompt = f"""
    Create a {days}-day travel itinerary for {destination}.
    Preferences: {preferences}.

    Make it clear, structured, and day by day.
    Make it concise. Maximum 8-10 lines per day.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"AI error: {str(e)}"
