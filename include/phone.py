from phonenumbers import parse, geocoder, carrier

def getInfo(phone):
    p = parse(phone)

    return {
        "city" : geocoder.description_for_number(p, "en"),
        "carrier" : carrier.name_for_number(p, "en")
    }