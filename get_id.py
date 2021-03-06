import http.client
import string
import json
import os

#Sets up HTTPS connection
conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")
#TOKEN = os.environ.get('IMDb',None)
TOKEN = "d8636faa8fmsh783aacbb586ca61p118b3cjsn4260967350bc"
headers = {
    'x-rapidapi-key': TOKEN,
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

def get_id(title):
    title=title.replace(" ", "%20")
    conn.request("GET", "/title/find?q="+title, headers=headers)
    # This converts json into dictionry to use in python
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))
    movie_id = data['results'][0]['id'][7:-1]
    if movie_id[0] == 'm':
            return -1
    return movie_id

def get_meta(movie_id):
    conn.request("GET", "/title/get-meta-data?ids="+movie_id, headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))
    return data