import urllib.request

def check():
    try:
        urllib.request.urlopen(url = "https://google.com")
        return True
    except:
        return False