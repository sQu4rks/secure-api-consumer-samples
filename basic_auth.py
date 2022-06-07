from email.policy import HTTP
import requests
from requests.auth import HTTPBasicAuth
import base64

BASE_URL = "https://sandboxdnac.cisco.com/dna"

PATH = "system/api/v1/auth/token"

auth = HTTPBasicAuth("<username>", "<password>")

url = f"{BASE_URL}/{PATH}"
resp = requests.post(url, auth=auth, verify=False)
print(resp.json())
