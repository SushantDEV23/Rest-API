import requests
import json

response=requests.post('https://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow')

for data in response.json()['items']:
    if data['answer_count']==2:
        print(data['title'])
        print(data['link'])
    #else:
     #   print("Just for checking purpose")