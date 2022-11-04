import requests

response = requests.get("http://127.0.0.1:5000/")
print (response.json())

response2 = requests.get("http://127.0.0.1:5000/Games")
print(response2.json())

response3 = requests.get("http://127.0.0.1:5000/GrandTheftAuto5")
print(response3.json())

a = {'game':'FootballManager2022','releaseYear':'2021','platform':'PC'}
response4 = requests.post("http://127.0.0.1:5000/Games", json=a)

response5 = requests.get("http://127.0.0.1:5000/FootballManager2022")
print(response5.json())

response6 = requests.get("http://127.0.0.1:5000/2018")
print(response6.json())

response7 = requests.get("http://127.0.0.1:5000/number/5")
print(response7.json())