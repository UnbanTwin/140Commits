import os
import random
from TwitterAPI import TwitterAPI
print(os.environ['CK'])
a = os.environ['CK']
b = os.environ['CSK']
c = os.environ['AK']
d = os.environ['ASK']
api = TwitterAPI(a,b,c,d)
with open('./words.txt') as f:
    wordOFChoice = random.choice(list(f))
    r = api.request('search/tweets', {'q':wordOFChoice+" -rt"+" -filter:links", 'lang':'en', 'count':'1'})
    
    for item in r:
        print(item['text'])


