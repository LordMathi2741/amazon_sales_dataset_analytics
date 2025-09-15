def price_formatter(price) -> float:
    patterns = "|,₹"
    for pattern in patterns:
        if pattern in price:
            price = price.replace(pattern, "")
    try:
        return float(price)
    except ValueError:
        return 0.0

def ratting_formatter(ratting) -> float:
    if "," in ratting:
        ratting = ratting.replace(",", ".")
    if "|" in ratting:
        ratting = ratting.replace("|", "")
    try:
        return float(ratting)
    except ValueError:
        return 0.0