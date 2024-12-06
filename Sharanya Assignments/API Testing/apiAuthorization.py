import json
import requests

from payLoad import register_client_payload
from utilities.configurations import *

# url = getconfig()["API"]["endpoint"]+"/products"
# response = requests.get(url,)
# print(response.text)
# print(type(response.text))
# dict_response = json.loads(response.text)
# print(type(dict_response))
# print(dict_response)
# json_response = response.json()
# print(json_response)
# print(type(json_response))
# assert response.status_code == 200
# assert response.headers['Content-Type'] == 'application/json; charset=utf-8'



register_client = requests.post("https://simple-tool-rental-api.glitch.me/api-clients",json = register_client_payload())
response = register_client.json()
print(response)
accessToken = response["accessToken"]
print(accessToken)

# Open the file in write mode
with open("authtoken.txt", "w") as file:
    file.write(accessToken)


