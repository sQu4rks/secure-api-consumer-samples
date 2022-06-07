import requests

BASE_URL = "https://sandboxdnac.cisco.com/dna"

PATH = "intent/api/v1/site/count"

TOKEN = "<insert token here>"


url = f"{BASE_URL}/{PATH}"

s = requests.Session()
s.headers.update({
    'X-Auth-Token': TOKEN
})
s.verify = False

resp = s.get(url)
print(resp.json())