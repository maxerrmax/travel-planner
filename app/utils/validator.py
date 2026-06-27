def validate_trip(destination, days, budget):
    destination = destination.strip()

    if len(destination) < 2:
        return "Destination is too short."

    if not (1 <= days <= 30):
        return "Trip must be between 1 and 30 days."

    if budget not in ["Low", "Medium", "High"]:
        return "Invalid budget."

    return None