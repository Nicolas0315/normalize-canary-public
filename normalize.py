def normalize(text):
    if not isinstance(text, str):
        raise TypeError("expected str")
    seen = set()
    result = []
    for part in text.split(","):
        token = part.strip().casefold()
        if not token or token in seen:
            continue
        seen.add(token)
        result.append(token)
    return result
