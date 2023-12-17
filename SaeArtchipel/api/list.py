import requests

endpoint = 'http://127.0.0.1:3000/auth/'
auth = requests.post(endpoint,json={'username':'root','password':'root'})
print(auth.json())

if auth.status_code == 200:
    token = auth.json()['token']
    print(token)
    headers = {'Authorization': 'Token ' + token}
endpoint = "http://127.0.0.1:3000/api/Lieu/"
response = requests.get(endpoint)

print(response.json())
print(response.status_code)