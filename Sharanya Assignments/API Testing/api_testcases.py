import os
import json
import logging
from apiMethods import *
from payLoad import create_order_payload, update_order_payload

with open("authtoken.txt", "r") as file:
    accessToken = file.read().strip()

header = {
    "Authorization" : f"Bearer {accessToken}",
    "Content-Type" : "application/json"
    }

def load_order_ids():
    try:
        with open("order_ids.json", "r") as file1:
            return json.load(file1)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_order_ids(order_ids):
    with open("order_ids.json", "w") as file1:
        json.dump(order_ids, file1, indent=4)

orderId = load_order_ids()

def get_all_tools():
    response = ApiMethods.get_request_method("tools")
    json_response = response.json()
    return response.status_code,json_response


def get_single_tool():
    response = ApiMethods.get_request_method("tools/4643")
    json_response = response.json()
    return response.status_code, json_response


# orderId = ["2nqyaJHV5cuppOQH8V9a5"]

def create_new_order():
    response = ApiMethods.post_request_method("orders",header, create_order_payload())
    json_response = response.json()
    new_order_id = json_response["orderId"]
    orderId.append(new_order_id)
    save_order_ids(orderId)
    return response.status_code, json_response


def get_all_orders():
    response = ApiMethods.get_request_method("orders",header)
    json_response = response.json()
    return response.status_code, json_response


def get_single_order():
    response = ApiMethods.get_request_method(f"/orders/{orderId[0]}",header)
    json_response = response.json()
    return response.status_code, json_response


def update_order():
    response = ApiMethods.patch_request_method(f"/orders/{orderId[1]}", header, update_order_payload())
    return response.status_code


def delete_order():
    response = ApiMethods.delete_request_method(f"/orders/{orderId[0]}", header)
    orderId.pop(0)
    save_order_ids(orderId)
    return response.status_code


if __name__ == "__main__":
    log_file = 'api_log.log'
    if not os.path.exists(log_file):
        open(log_file, 'w').close()

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
    )

    response = get_all_tools()
    logging.info(f'Get All Tools: {json.dumps(response, indent=4)}')
    print(response)

    response = get_single_tool()
    logging.info(f'Get Single Tools: {json.dumps(response, indent=4)}')
    print(response)

    response = create_new_order()
    logging.info(f'Create New Order: {json.dumps(response, indent=4)}')
    print(response)

    response = get_all_orders()
    logging.info(f'Get All Orders: {json.dumps(response, indent=4)}')
    print(response)

    response = get_single_order()
    logging.info(f'Get Single Order: {json.dumps(response, indent=4)}')
    print(response)

    response = update_order()
    logging.info(f'Update Order: {json.dumps(response, indent=4)}')
    print(response)

    response = delete_order()
    logging.info(f'Delete Order: {json.dumps(response, indent=4)}')
    print(response)

