import urllib.request
from json import loads

def getInfo(bin):
    try:
        r = urllib.request.urlopen(url = f"https://lookup.binlist.net/{bin}")
        
        j = loads(r.read())

        try:
            type = j['type']
        except:
            type = "Not found!"

        try:
            prepaid = j['prepaid']
        except:
            prepaid = "Not found!"

        try:
            country = j['country']['name']
        except:
            country = "Not found!"

        try:
            bank = j['bank']['name']
        except:
            bank = "Not found!"

        return {"type" : type,
                "prepaid" : prepaid,
                "country" : country,
                "bank" : bank}
    
    except urllib.error.HTTPError:
        return False