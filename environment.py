import os

token = os.environ.get('TOKEN')
if not token:
    print("Missing auth token")
print(token)