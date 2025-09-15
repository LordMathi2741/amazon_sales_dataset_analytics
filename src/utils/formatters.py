def price_formatter(price) -> float:
    try:
        patterns = "|,₹"
        for pattern in patterns:
            if pattern in price:
                price = price.replace(pattern, "")
            return float(price)
    except ValueError:
        return 0.0

def ratting_formatter(ratting) -> float:
    try:
        if "," in ratting:
            ratting = ratting.replace(",", ".")
        if "|" in ratting:
            ratting = ratting.replace("|", "")
        return float(ratting)
    except ValueError:
        return 0.0