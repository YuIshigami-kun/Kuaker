from requests import get
from json import loads

def getInfo(ip):
    r = get(url = "http://ip-api.com/json/" + ip)
    rr = loads(r.text)

    return rr