from win32com.client import Dispatch
from newsapi import NewsApiClient
import requests
import json
newsapi = NewsApiClient(api_key='93aa36a48c83413ba9553ea1cf609c7f')

def read_headlines(headlines):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(headlines)

if __name__ == '__main__':
    url =  ('https://newsapi.org/v2/top-headlines?'
           'sources=bbc-sport&'
           'apiKey=93aa36a48c83413ba9553ea1cf609c7f')

    response = requests.get(url)
    text = response.text
    json_data = json.loads(text)
    print(json_data)
    for data in range(0, 11):
        read_headlines(json_data['articles'][data]['title'])
