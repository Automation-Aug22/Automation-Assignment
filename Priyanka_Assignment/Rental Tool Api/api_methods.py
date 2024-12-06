import requests

class ApiMethods:
    base_url = 'https://simple-tool-rental-api.glitch.me'

    @staticmethod
    def get(endpoint, params=None, headers=None):
        """ Send a GET request to the API """
        response = requests.get(f"{ApiMethods.base_url}/{endpoint}", params=params, headers=headers)
        return response

    @staticmethod
    def post(endpoint, data=None, headers=None):
        """ Send a POST request to the API """
        response = requests.post(f"{ApiMethods.base_url}/{endpoint}", json=data, headers=headers)
        return response

    @staticmethod
    def patch(endpoint, data=None, headers=None):
        """ Send a PATCH request to the API """
        response = requests.patch(f"{ApiMethods.base_url}/{endpoint}", json=data, headers=headers)
        return response

    @staticmethod
    def delete(endpoint, headers=None):
        """ Send a DELETE request to the API """
        response = requests.delete(f"{ApiMethods.base_url}/{endpoint}", headers=headers)
        return response
