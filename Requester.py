import requests
response = requests.get("http://127.0.0.1:5000/Games")
print(response.json())

response2 = requests.get("http://127.0.0.1:5000/GrandTheftAuto5")
print(response2.json())

a = {'game':'FootballManager2022','releaseYear':'2021','platform':'PC'}
response3 = requests.post("http://127.0.0.1:5000/Games", json=a)

response4 = requests.get("http://127.0.0.1:5000/FootballManager2022")
print(response4.json())

response5 = requests.get("http://127.0.0.1:5000/2018")
print(response5.json())