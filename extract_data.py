import requests
import pandas as pd

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

querystring = {"formatType":"test"}

headers = {
	"x-rapidapi-key": "d11b43727fmshe0f582982c875d2p1e2068jsn13da52b29c0a",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

columns = ['rank', 'name', 'country', 'rating']


for each in response.json().get('rank'):
    print(each['name'])