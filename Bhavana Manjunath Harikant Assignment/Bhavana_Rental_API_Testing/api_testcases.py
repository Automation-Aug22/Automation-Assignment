import json
import logging
import os


from http_methods import ApiMethods

def check_status(code):
    if code==200:
        print(f"We got status code{code}:Indicates a successful response.")
    elif code==400:
        print(f"We got status code{code}:Indicates that the parameters provided are invalid.")
    elif code==404:
        print(f"We got status code{code}:Indicates that there is no tool or order with the specified id.")
    elif code==401:
        print(f"We got status code{code}:Indicates that request has not been authenticated. Check the response body for additional details.")
    elif code==201:
        print(f"We got status code{code}:Indicates that the order has been created successfully.")
    elif code==204:
        print(f"We got status code{code}:Indicates that successfull message.")
    elif code==409:
        print("Indicates that an API client has already been registered with this email address.")





def insert_dict_to_json(file_path, new_dict):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump([], file)

    with open(file_path, 'r') as file:
        data = json.load(file)

    data.append(new_dict)

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def fetch_last_entry_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        if data:
            return data[-1]
        else:
            return None

    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {file_path}.")
        return None

def clear_json_file(file_path):
    with open(file_path, 'w') as file:
        json.dump([], file)

def fetch_auth_token_from_file(filename='auth_token.txt'):
    try:
        with open(filename, 'r') as file:
            auth_token = file.read().strip()  # .strip() to remove any extra whitespace or newlines
            return auth_token
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

def clear_logfile(file_path):
    with open(file_path, 'w') as file:
        file.truncate(0)  # Clears the content of the file
        print(f"The log file at {file_path} has been cleared.")

def status_check():
    try:
        response=ApiMethods.get("status")
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_all_tools(params=None):
    try:
        response=ApiMethods.get("tools",params)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_single_tool(toolID):
    try:
        url=f'tools/{toolID}'
        response = ApiMethods.get(url)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_all_order(a_token):
    try:
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Content-Type': 'application/json'
        }
        response=ApiMethods.get("orders",headers=headers)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def create_a_new_order(auth_token,json_data):
    try:
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Content-Type': 'application/json'
        }

        response = ApiMethods.post("orders", json=json_data, headers=headers)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def update_an_order(a_token,orderID):
    try:
        custemer_name=input("Enter the customer name to update the previous one:")
        json_data={
            "customerName": custemer_name
        }
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Content-Type': 'application/json'
        }
        url=f'orders/{orderID}'
        response=ApiMethods.patch(url,json=json_data,headers=headers)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_a_single_order(a_token,orderID):
    try:
        url = f'orders/{orderID}'
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Content-Type': 'application/json'
        }
        response=ApiMethods.get(url,headers=headers)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def delete_order(a_token,orderID):
    try:
        url = f'orders/{orderID}'
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Content-Type': 'application/json'
        }
        response=ApiMethods.delete(url,headers=headers)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    log_file = 'api_status.log'
    if not os.path.exists(log_file):
        open(log_file, 'w').close()

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
    )

    json_file_path1='data_order.json'
    if not os.path.exists(json_file_path1):
        with open(json_file_path1,'w') as file:
            json.dump([],file)

    json_file_path2 = 'data_tool.json'
    if not os.path.exists(json_file_path2):
        with open(json_file_path2, 'w') as file:
            json.dump([], file)


    auth_token = fetch_auth_token_from_file()
    if auth_token:
        print(f"Auth Token fetched from file: {auth_token}")
    else:
        print("No token found.")

    answ = input("If you want to clear the log file enter Y/y:")

    if answ.lower() == 'y':
        clear_logfile(log_file)

    print()

    #Status Check Response
    print("'Status Check Response':")
    response=status_check()
    print("Status Code:",response.status_code)
    check_status(response.status_code)
    logging.info(f"Status Code: {response.status_code}")
    print("Text Response:",response.text)
    logging.info(f"Text response: {response.text}")
    json_responses = response.json()
    logging.info(f'Status Check Response JSON: {json.dumps(json_responses, indent=4)}')
    print()


    #Get all tools
    print("'Get all tools':")
    response=get_all_tools()
    print("Status Code:", response.status_code)
    check_status(response.status_code)
    logging.info(f"Status Code: {response.status_code}")
    print("Text Response:", response.text)
    logging.info(f"Text response: {response.text}")
    json_responses = response.json()
    logging.info(f'Get all tools Response JSON: {json.dumps(json_responses, indent=4)}')
    print()

    # Get all tools
    print("'Get all tools':")
    param={
        'category':'ladders',
        'results':'10'
    }
    response = get_all_tools(param)
    print("Status Code:", response.status_code)
    logging.info(f"Status Code: {response.status_code}")
    check_status(response.status_code)
    print("Text Response:", response.text)
    logging.info(f"Text response: {response.text}")
    json_responses = response.json()
    insert_dict_to_json(json_file_path2,json_responses)
    last_item=fetch_last_entry_from_json(json_file_path2)
    # print("Last item:",last_item)
    toolID=last_item[-1]['id']
    logging.info(f'Get all tools Response JSON: {json.dumps(json_responses, indent=4)}')
    print()

    #Get single tool
    print("'Get single tool':")
    toolID=4643
    response = get_single_tool(toolID)
    print("Status Code:", response.status_code)
    check_status(response.status_code)
    logging.info(f"Status Code: {response.status_code}")
    print("Text Response:", response.text)
    logging.info(f"Text response: {response.text}")
    json_responses = response.json()
    logging.info(f'Get single tools Response JSON: {json.dumps(json_responses, indent=4)}')
    print()

    # Create a new order
    json_data = {
        "toolId": 2177,
        "customerName": "Bhavana Harikant"
    }
    print("Create a new order")
    response=create_a_new_order(auth_token,json_data)
    print("Status Code:", response.status_code)
    check_status(response.status_code)
    logging.info(f"Status Code: {response.status_code}")
    print("Text Response:", response.text)
    logging.info(f"Text response for create new order: {response.text}")
    json_responses = response.json()
    insert_dict_to_json(json_file_path1,json_responses)
    logging.info(f'Get single tools Response JSON: {json.dumps(json_responses, indent=4)}')
    print()

    #Get all orders
    print("'Get all orders':")
    response = get_all_order(auth_token)
    print("Status Code:", response.status_code)
    check_status(response.status_code)
    logging.info(f"Status Code: {response.status_code}")
    print("Text Response for get all orders:", response.text)
    logging.info(f"Text response: {response.text}")
    json_responses = response.json()
    logging.info(f'Get all orders Response JSON: {json.dumps(json_responses, indent=4)}')
    print()

    # Get a single order
    print("'Get a single order':")
    last_order = fetch_last_entry_from_json(json_file_path1)
    orderID=last_order['orderId']
    response = get_a_single_order(auth_token, orderID)
    print("Status Code:", response.status_code)
    check_status(response.status_code)
    logging.info(f"Status Code: {response.status_code}")
    print("Text Response:", response.text)
    logging.info(f"Text response: {response.text}")
    json_responses = response.json()
    logging.info(f'Get an single order Response JSON: {json.dumps(json_responses, indent=4)}')
    print()

    #Update an order
    print("'Update an order':")
    response=update_an_order(auth_token,orderID)
    print("Status Code:", response.status_code)
    check_status(response.status_code)
    logging.info(f"Status Code: {response.status_code}")
    print("Text Response:", response.text)
    print()

    #Get a single order
    print("'Get a single order':")
    response=get_a_single_order(auth_token,orderID)
    print("Status Code:", response.status_code)
    check_status(response.status_code)
    logging.info(f"Status Code: {response.status_code}")
    print("Text Response:", response.text)
    logging.info(f"Text response: {response.text}")
    json_responses = response.json()
    logging.info(f'Get an updated order Response JSON: {json.dumps(json_responses, indent=4)}')
    print()

    #Delete an order
    print("'Delete an order':")
    response=delete_order(auth_token,orderID)
    print("Status Code:", response.status_code)
    check_status(response.status_code)
    logging.info(f"Status Code: {response.status_code}")
    print()

    userip = input("If you want to clear the JSON file enter Y/y:")

    if userip.lower() == 'y':
        clear_json_file(json_file_path1)
        clear_json_file(json_file_path2)
