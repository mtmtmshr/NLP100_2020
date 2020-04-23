import requests
import json


params = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File:Flag of the United Kingdom.svg",
    "iiprop": "url"
    }
S = requests.Session()
URL = "https://www.mediawiki.org/w/api.php"
R = S.get(url=URL, params=params)
DATA = R.json()
print(DATA["query"]["pages"]["-1"]["imageinfo"][0]["url"])
