def clean_data(data):
    result = {}

    if "style" in data:
        result["style"] = data["style"].strip().lower()

    if "size" in data:
        result["size"] = data["size"].strip().upper()

    if "shoe_size" in data:
        try:
            result["shoe_size"] = int(data["shoe_size"])
        except:
            result["shoe_size"] = None

    return result