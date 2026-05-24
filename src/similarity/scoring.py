def calculate_score(vendor, user):

    score = 0
    reasons = []

    # Category Match
    if vendor["category"] == user["category"]:
        score += 40
        reasons.append("Matching category")

    # Location Match
    if vendor["location"] == user["location"]:
        score += 25
        reasons.append("Same location")

    # Delivery Match
    if vendor["delivery"] == user["delivery"]:
        score += 20
        reasons.append("Preferred delivery available")

    # Budget Similarity
    difference = abs(
        vendor["budget"] - user["budget"]
    )

    if difference <= 10000:
        score += 15
        reasons.append("Fits budget range")

    elif difference <= 30000:
        score += 8
        reasons.append("Near budget range")

    return score, reasons