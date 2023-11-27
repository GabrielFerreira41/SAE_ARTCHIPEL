import requests

endpoint = 'http://127.0.0.1:8000/auth/'
auth = requests.post(endpoint,json={'username':'root','password':'azerty28'})
print(auth.json())
print(auth.status_code)
if auth.status_code == 200:
    token = auth.json()['token']
    print(token)
    headers = {'Authorization': 'Token ' + token}
endpoint = "http://127.0.0.1:8000/api/Lieu/"
response = requests.get(endpoint,headers=headers)

print(response)
print(response.json())
print(response.status_code)