import requests
import json

x = requests.get('https://mern-capstone.herokuapp.com/api/bugs')
print(x)
data = x.text
print(json.loads(data))


