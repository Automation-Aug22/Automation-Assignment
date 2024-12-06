import json
import logging
import os
from api_methods import ApiMethods
# Log file to store API responses
log_file = 'order_details.log'
def fetch_first_entry_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        if data:
            return data[-1]
        else:
            return None
    except Exception as e:
        print(f"Error occurred while fetching the data: {e}")
def save_response_to_json(file_path, response_data):
    # Check if the file exists
    if not os.path.exists(file_path):
        # If the file does not exist, create it with an empty list
        with open(file_path, 'w') as file:
            json.dump([], file)
    # Load existing data from the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    # Append the new response data to the existing data
    data.append(response_data)
    # Save the updated data back to the JSON file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
# Function to fetch the auth token from a file
def fetch_auth_token_from_file(filename='auth_token.txt'):
    try:
        with open(filename, 'r') as file:
            auth_token = file.read().strip()  # .strip() to remove any extra whitespace or newlines
            return auth_token
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
# Function to clear the log file before new operations
def clear_logfile(file_path):
    with open(file_path, 'w') as file:
        file.truncate(0)  # Clears the content of the file
        print(f"The log file at {file_path} has been cleared.")
# Function to log API responses to a file
def log_response(method, url, status_code, response_data):
    """ Logs the API response to a log file. """
    with open(log_file, 'a') as log:
        log.write(f"Method: {method} | URL: {url} | Status Code: {status_code} | Response: {response_data}\n")
# Test for checking the API status
def test_status_check():
    try:
        response = ApiMethods.get("status")
        print("Status Code:", response.status_code)
        assert response.status_code == 200
        log_response('GET', 'status', response.status_code, response.json())
        print("API Response:", response.json())
    except Exception as e:
        print(f"An error occurred: {e}")
        log_response('GET', 'status', 500, str(e))
# Test for fetching all tools
def test_fetch_tools():
    try:
        response = ApiMethods.get("tools")
        assert response.status_code == 200
        log_response('GET', 'tools', response.status_code, response.json())
        print("Fetched Tools:", json.dumps(response.json(), indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")
        log_response('GET', 'tools', 500, str(e))
# Test for creating a new order
def test_create_order():
    token = fetch_auth_token_from_file()  # Fetch the auth token
    if token:
        data = {
            "toolId": 5499,
            "customerName": "John Doe"
        }
        headers = {'Authorization': f'Bearer {token}'}
        try:
            response = ApiMethods.post("orders", data=data, headers=headers)
            assert response.status_code == 201
            log_response('POST', 'orders', response.status_code, response.json())
            print("Order Created:", json.dumps(response.json(), indent=4))
            save_response_to_json('order1_history.json', response.json())
        except Exception as e:
            print(f"An error occurred: {e}")
            log_response('POST', 'orders', 500, str(e))
    else:
        print("Authorization token is missing.")
# Test for updating an order
def test_update_order():
    token = fetch_auth_token_from_file()  # Fetch the auth token
    first_order = fetch_first_entry_from_json('order1_history.json')
    if first_order:
        order_id = first_order['orderId']
        if token:
            data = {
                "customerName": "Jane Doe"
            }
            headers = {'Authorization': f'Bearer {token}'}
            try:
                response = ApiMethods.patch(f"orders/{order_id}", data=data, headers=headers)
                print("Status code:",response.status_code)
                if response.status_code != 204:  # Handle non-204 status
                    log_response('PATCH', f'orders/{order_id}', response.status_code, response.json())
                    print("Order Updated:", json.dumps(response.json(), indent=4))
                else:
                    log_response('PATCH', f'orders/{order_id}', response.status_code, "No Content")
                    print("Order Updated: No Content Response")
            except Exception as e:
                print(f"An error occurred: {e}")
                log_response('PATCH', f'orders/{order_id}', 500, str(e))
        else:
            print("Authorization token is missing.")
# Test for deleting an order
def test_delete_order():
    token = fetch_auth_token_from_file()
    first_order = fetch_first_entry_from_json('order1_history.json')
    if first_order:
        order_id = first_order['orderId']
        # Fetch the auth token
        if token:
            headers = {'Authorization': f'Bearer {token}'}
            try:
                response = ApiMethods.delete(f"orders/{order_id}", headers=headers)
                print("Status code:", response.status_code)
                if response.status_code != 204:  # Handle non-204 status
                    log_response('DELETE', f'orders/{order_id}', response.status_code, response.json())
                    print("Order Deleted:", json.dumps(response.json(), indent=4))
                else:
                    log_response('DELETE', f'orders/{order_id}', response.status_code, "No Content")
                    print("Order Deleted: No Content Response")
            except Exception as e:
                print(f"An error occurred: {e}")
                log_response('DELETE', f'orders/{order_id}', 500, str(e))
        else:
            print("Authorization token is missing.")
# Run the tests
if __name__ == "__main__":
    # Clear the previous log file before starting new operations
    clear_logfile(log_file)
    # Execute all test operations
    test_status_check()
    test_fetch_tools()
    test_create_order()
    test_update_order()
    test_delete_order()
