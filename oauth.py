import json
from flask import Flask, request
from webexteamssdk import WebexTeamsAPI
import requests

credentials = json.load(open("integration_credentials.json"))
app = Flask(__name__)

@app.route('/auth')
def auth():
    return f"<a href='{credentials['url']}'>Auth</a>"

@app.route('/oauth')
def oauth():
    args = request.args
    code = args.get('code')

    url = "https://webexapis.com/v1/access_token"
    headers = {
        'accept': "application/json",
        'content-type': "application/x-www-form-urlencoded"
    }

    payload = {
        'client_id': credentials['client_id'],
        'client_secret': credentials['client_secret'],
        'code': code,
        'redirect_uri': credentials['redirect_url'],
        'grant_type': "authorization_code"
    }

    resp = requests.post(url, data=payload, headers=headers)
    if resp.ok:
        api = WebexTeamsAPI(access_token=resp.json()['access_token'])
        return str(api.people.me())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
