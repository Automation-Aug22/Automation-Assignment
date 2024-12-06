'''
API Documentation Link :
https://github.com/vdespa/quick-introduction-to-postman/blob/main/simple-tool-rental-api.md#Update-an-order
'''

import requests
import json

class API:
    base_url = "https://simple-tool-rental-api.glitch.me"

    def get_methods(endpoint, params = None, headers = None):
        response = requests.get(f'{API.base_url}/{endpoint}', params=params, headers=headers)
        return response

    def post_methods(endpoint, json = None, headers = None):
        response = requests.post(f'{API.base_url}/{endpoint}', json = json, headers=headers)
        return response

    def patch_methods(endpoint, data = None, json = None, headers = None):
        response = requests.patch(f'{API.base_url}/{endpoint}', data = data, json = json, headers=headers)
        return response

    def delete_methods(endpoint, data = None, json = None, headers = None):
        response = requests.delete(f'{API.base_url}/{endpoint}', data = data, json = json, headers=headers)
        return response