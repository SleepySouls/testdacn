import requests

def make_authorized_request():
    url = 'http://127.0.0.1:8000/signin/login_user/get_current_user_id'
    params = {
        'current_user': 'admin'
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

print(make_authorized_request())