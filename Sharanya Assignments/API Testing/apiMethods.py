import requests

class ApiMethods:
    baseurl = "https://simple-tool-rental-api.glitch.me"

    @staticmethod
    def get_request_method(endpoint,headers=None,params=None):
        response = requests.get(f"{ApiMethods.baseurl}/{endpoint}", headers=headers, params=params)
        return response

    @staticmethod
    def post_request_method(endpoint,headers=None,json=None):
        response = requests.post(f"{ApiMethods.baseurl}/{endpoint}", headers=headers, json=json)
        return response

    @staticmethod
    def patch_request_method(endpoint, headers=None, json=None):
        response = requests.patch(f"{ApiMethods.baseurl}/{endpoint}", headers=headers, json=json)
        return response

    @staticmethod
    def delete_request_method(endpoint, headers=None, json=None):
        response = requests.delete(f"{ApiMethods.baseurl}/{endpoint}", headers=headers, json=json)
        return response

