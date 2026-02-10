import requests

parm={
        "name":"Abhi"
    }
response=requests.get(url="https://api.genderize.io",params=parm)
data=response.json()
print(data)
print(data["gender"])
