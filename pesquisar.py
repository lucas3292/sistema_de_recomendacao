import re
import requests
import json

req = requests.get('http://www.steamspy.com/api.php?request=all')
dic = json.loads(req.text)
results = []
for appid in dic:
    jogo = dic[appid]
    if ("PARTY JOUSTING" in jogo['name'].upper()):
        results.append(jogo)
print(results)

