# Write a program that fetches and prints out a random Chuck Norris joke for the user. Use the API presented here:
#  https://api.chucknorris.io/. The user should only be shown the joke text.


import requests

url = "https://api.chucknorris.io/jokes/random"

try:
    data = requests.get(url)

    if data.status_code == 200:
        fetchedData = data.json()
        print("Joke: "+ fetchedData["value"])

    else:
        print("Error")
except requests.exceptions.RequestException:
    print("Error while fetching the data")