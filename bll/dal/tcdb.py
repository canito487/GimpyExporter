import requests
import simplejson as json

def login_gimpy_call(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=json.dumps(body), headers=headers)
    return response

def add_a_test_case_call(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=json.dumps(body), headers=headers)
    return response

def update_feature_suite_call(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.put(url, data=json.dumps(body), headers=headers)
    return response
