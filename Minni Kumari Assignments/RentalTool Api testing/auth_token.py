#import requests
#post_response = requests.post('https://simple-tool-rental-api.glitch.me/api-clients', json={
  #  "clientName": "Postman",
    #"clientEmail": "enti6n@example.com"
#}, headers={"Content-Type": "application/json"})
#json_res=post_response.json()
#api_token=json_res['accessToken']
#file_name='auth_token.txt'
#with open(file_name,'w') as file:
    #file.write(api_token)
#print(post_response.json())


import requests
import json
response = requests.post('https://simple-tool-rental-api.glitch.me/api-clients',json={
    "clientName": "Postman",
    "clientEmail": "vai123564@example.com"
})
#it gives the code of error
print(response)
# print(response.text)
response_json = response.json()
# dict_response = json.loads(response.text)
api_token=response_json['accessToken']
file_name='auth_token.txt'

with open(file_name, 'w') as file:
    file.write(api_token)

print(response_json)