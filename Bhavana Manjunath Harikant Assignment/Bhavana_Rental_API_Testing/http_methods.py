import requests

class ApiMethods:
    base_url = 'https://simple-tool-rental-api.glitch.me'

    @staticmethod
    def get(endpoint, params=None, headers=None):
        response = requests.get(f"{ApiMethods.base_url}/{endpoint}", params=params, headers=headers)
        return response

    @staticmethod
    def post(endpoint, data=None, json=None, headers=None):
        response = requests.post(f"{ApiMethods.base_url}/{endpoint}", data=data, json=json, headers=headers)
        return response

    @staticmethod
    def patch(endpoint, data=None, json=None, headers=None):
        response = requests.patch(f"{ApiMethods.base_url}/{endpoint}", data=data, json=json, headers=headers)
        return response

    @staticmethod
    def delete(endpoint, params=None, headers=None):
        response = requests.delete(f"{ApiMethods.base_url}/{endpoint}", params=params, headers=headers)
        return response
