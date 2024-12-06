'''
API Documentation Link :
https://github.com/vdespa/quick-introduction-to-postman/blob/main/simple-tool-rental-api.md#Update-an-order
'''

import logging
import json
from apiValidations import API

def get_allTools(params = None):
    response = API.get_methods("tools", params)
    json_format = response.json()
    print(f'Get all Tools. \nStatus code is: {response.status_code} \t')
    if response.status_code == 200:
        print(f'{response.status_code} indicates a successful response. \t')
        return json_format

    else:
        print(f'{response.status_code} Indicates that the parameters provided are invalid.')
        return None

    # return json_format

def get_singleTool(toolID):
    url = f'tools/{toolID}'
    response = API.get_methods(url)
    json_format = response.json()
    print(f'Get Single Tool. \nStatus code is: {response.status_code} \t')
    if response.status_code == 200:
        print(f'{response.status_code} indicates a successful response. \t')
        return json_format
    else:
        print(f'{response.status_code} Indicates that there is no tool with the specified id.')
        return None

''' def generate_accesstoken():
    data = {
   "clientName": "Trial",
   "clientEmail": "anjalitest1@example.com"
}
    response = API.post_methods("api-clients", json = data, )
    print(response.status_code)
    print(response.json())

generate_accesstoken() '''

def getAllOrders(accessToken, params = None):
    # headers = {'Authorization' : f'Bearer {accessToken}'}
    response = API.get_methods("orders", params = params, headers = headers)
    print(f'Get all Orders. \nStatus code is: {response.status_code} \t')
    if response.status_code == 200:
        print(f'{response.status_code} indicates a successful response. \t')
        return response.json()

    else:
        print(f'{response.status_code} Indicates that request has not been authenticated. Check the response body for additional details.')
        return None

def create_newOrder(headers):
    data = {
        "toolId": 4643,
        "customerName": "Anjali M"
    }
    response = API.post_methods("orders", json = data, headers=headers)
    print(f'Create new Order. \nStatus code is: {response.status_code} \t')
    if response.status_code == 201:
        print(f'{response.status_code} Indicates that the order has been created successfully.')
        return response.json()

    elif response.status_code == 400:
        print(f'{response.status_code} Indicates that the parameters provided are invalid.')
        return None

    else:
        print(f'{response.status_code} Indicates that request has not been authenticated. Check the response body for additional details.')
        return None

def getSingleOrder(orderId,):
    response = API.get_methods(f'orders/{orderId}', headers=headers)
    print(f'Getting Single Order. \nStatus code is: {response.status_code} \t')
    if response.status_code == 200:
        print(f'{response.status_code} Indicates a successful response.')
        return response.json()

    elif response.status_code == 401:
        print(f'{response.status_code} Indicates that request has not been authenticated. Check the response body for additional details.')
        return None

    else:
        print(f'{response.status_code} Indicates that there is no order with the specified id associated with the API client.')
        return None

def updateName(accessToken, orderID, headers):
    name = {"customerName": "Wilcent Doe"}
    response = API.patch_methods(f'orders/{orderID}', json = name, headers=headers )

    print(f'Updating Order. \nStatus code is: {response.status_code} \t')
    if response.status_code == 204:
        print("No content returned. Indicates that the order has been updated successfully. \n")
        return None

    elif response.status_code == 200:
        try:
            # Attempt to parse the response as JSON
            return response.json()
        except ValueError:
            print("Error parsing JSON. Response content might not be in JSON format.")
            return None
    else:
        # Print the response text to see the raw response in case of an error
        print(f"Failed to update order. Status code: {response.status_code}")
        print("Response content:", response.text)
        return None

def deleteOrder(order_Id, accessToken, headers):
    response = API.delete_methods(f'orders/{order_Id}', headers=headers)
    print(f'Deleting Order. \nStatus code is: {response.status_code} \t')
    if response.status_code == 204:
        print("Order deleted successfully. \n")
        response = API.get_methods("orders", params=params, headers=headers)
        print(f'Getting all orders. \nStatus code is: {response.status_code} \t')
        return response.json()
    elif response.status_code == 400:
        print(f'{response.status_code} Indicates that the parameters provided are invalid.')
        return None
    elif response.status_code == 401:
        print(f'{response.status_code} Unauthorised. Indicates that request has not been authenticated. Check the response body for additional details.')
        return None
    else:
        print(f"{response.status_code} Indicates that there is no order with the specified id associated to the API client.")
        return None

def clear_logFile(logfile):
    with open(logfile, 'w') as file:
        file.truncate(0)
    print(f"The data in the file {logfile} is cleared")


if __name__ == "__main__":
    accessToken = "21bb9af4d7bb94647a8a4d58042698edeac3bc9cf2722b32e235ac792169ae69"
    headers = {'Authorization': f'Bearer {accessToken}'}
    logfile = 'api_response.log'
    logging.basicConfig(filename=logfile,
                        level=logging.INFO,
                        format='%(asctime)s - %(message)s, ')

    #clearing the Log file
    clear_file = input("Clear result file ? (Y/y)")
    if clear_file.lower() == "y":
        clear_logFile(logfile)

    #get all tools with a category parameter.
    params = {'category' : 'plumbing'}
    response = get_allTools(params)
    print(f"List of all the tools: {response} \n")
    logging.info(f'Following is the json Response: \n List of all the tools: {json.dumps(response, indent=4)}')

    #get a single tool
    toolID = 2177
    response2 = get_singleTool(toolID)
    print(f'Single tool with tooID : {toolID}: {response2} \n')
    logging.info(f'Single tool with tooID : {toolID}: {json.dumps(response2, indent=4)}')

    # creating an order.
    order = create_newOrder(headers)
    if order:
        print("Order created successfully:", json.dumps(order, indent=4))
    else:
        print("Failed to create an order.")

    # get all orders.
    response3 = getAllOrders(accessToken)
    print(f'List of all the orders: {response3} \n')
    logging.info(f'List of all the orders: {json.dumps(response3, indent=4)}')

    #single order
    orderId = "acmQzqfvNvUybiDaLyyUk"
    response4 = getSingleOrder(orderId)
    print(f'Single order with orderID : {orderId}:- {response4} \n')
    logging.info(f'Single order with orderID : {orderId}:- {json.dumps(response4, indent=4)}')

    #updating order
    orderID = "z7s_5ioBSQLMK08B_I9F9"
    updated = updateName(accessToken, orderID, headers)
    response5 = getSingleOrder(orderID)
    print(f'Updated order response: {response5} \n')
    logging.info(f'Updated order response: {json.dumps(response5, indent=4)}')

    #deleting the Order
    order_Id = "_b15MEtbXes5MeyL9AYrl"
    delete_order = deleteOrder(order_Id, accessToken, headers)
    print(f'Order response, after deletion of {order_Id}: {delete_order} \n')
    logging.info(f'Order response, after deletion of {order_Id}: {json.dumps(delete_order, indent=4)}')


