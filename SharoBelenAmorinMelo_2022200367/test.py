import requests
response = requests.post('http://localhost:5003/cliente', json={"id":"4133266"})
print(response.json())
response = requests.post('http://localhost:5003/cliente', json={"ci":"5661688"})
print(response.json())