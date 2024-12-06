from http_methods import ApiMethods


def main():
    json_value = {
        "clientName": "Postman",
        "clientEmail": "bhava1234@example.com"
    }

    response = ApiMethods.post("api-clients", json=json_value)

    print("Response Code:", response.status_code)
    print("Response Body:", response.text)

    json_responses = response.json()
    api_token = json_responses['accessToken']
    with open('auth_token.txt', 'w') as file:
        file.write(api_token)
    return api_token

if __name__ == "__main__":
    main()
